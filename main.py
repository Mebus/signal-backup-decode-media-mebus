#!/usr/bin/python

import os
import shutil
import sqlite3
import sys


class SortSignal:

    # EDIT: do some configuration here according to your needs
    sqlitefile = "../signal-2019-05-28-15-32-37.sqlite"  # path to the sqlite database
    attachment_path = (
        "../signal-2019-05-28-15-32-37/attachments"
    )  # where you extracted the attachments

    dryrun = True  # do not move the files
    move_instead_of_copy = False  # move the files if if True, not just copy

    # DONOTEDIT:
    groupname = ""
    targetdir = "mytargetdir"

    def connect(self):
        self.conn = sqlite3.connect(self.sqlitefile)
        self.c = self.conn.cursor()
        self.d = self.conn.cursor()

    def get_part(self, mid, date):
        res = self.d.execute(
            "SELECT unique_id, ct, _id FROM part WHERE mid=" + str(mid) + ";"
        )
        for r in res:

            unique_id = r[0]  # unique ID (is in file name)
            ct = r[1]  # Mime type
            id = r[2]  # part id

            filename = str(unique_id) + "_" + str(id)
            self.move_file(filename, ct, date)

    def main(self, thread_id, targetdir):

        self.thread_id = thread_id
        self.targetdir = targetdir

        self.connect()

        ## get all MMS'es for the thread and request the parts
        sql = "SELECT _id, date FROM mms WHERE thread_id=" + str(thread_id) + ";"
        print(sql)
        res = self.c.execute(sql)

        for r in res:
            mid = r[0]
            date = r[1]
            print(mid)

            self.get_part(mid, date)

    # Helpers
    def file_ending_for_mime(self, mime):

        ending = ""

        if mime == "image/png":
            ending = ".png"
        elif mime == "image/jpeg":
            ending = ".jpg"
        elif mime == "audio/x-hx-aac-adts":
            ending = ".wav"
        elif mime == "image/gif":
            ending = ".gif"
        elif mime == "video/mp4":
            ending = ".mp4"
        elif mime == "application/pdf":
            ending = ".pdf"
        elif mime == "audio/aac":
            ending = ".mp4"

        return ending

    def move_file(self, filename, mime, date):

        filepath = os.path.join(self.attachment_path, filename)
        print(filepath)

        ending = self.file_ending_for_mime(mime)

        newfilename = "date-" + str(date) + "_uniquteid-" + filename + ending
        full_newfilename = os.path.join(self.targetdir, newfilename)
        print(full_newfilename)

        if os.path.isfile(filepath):

            print("file exists :-)")

            if not os.path.isdir(self.targetdir):
                print("creating directory " + self.targetdir)
                os.mkdir(self.targetdir)

            if not self.dryrun:

                if self.move_instead_of_copy:
                    shutil.move(filepath, full_newfilename)
                else:
                    shutil.copy2(filepath, full_newfilename)

        else:

            print("File does not exist :-(")


if __name__ == "__main__":

    srt = SortSignal()

    # set the Thread-ID you want to extract and the Target-Directory
    srt.main(10, "Anna")
    srt.main(78, "HackerFriends")
