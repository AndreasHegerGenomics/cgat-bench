"""purge a benchmarking run from the database.

This tool is for removing outputs, logs and metrics generated by daisy
run.

"""

import sys
import daisy.Experiment as E
import daisy.Storage as Storage


def main(argv=None):

    parser = E.OptionParser(version="%prog version: $Id$",
                            usage=globals()["__doc__"])

    parser.add_option(
        "-r", "--run-id", dest="run_id", type="int",
        help="numerical identifier of a run [%default]")

    parser.add_option(
        "-d", "--database-url", dest="database_url", type="string",
        help="database url [%default]"
    )

    parser.add_option(
        "-n", "--dry-run", dest="dry_run", action="store_true",
        help="only show statements to be executed [%default]"
    )

    parser.set_defaults(
        run_id=None,
        database_url="sqlite:///./csvdb",
        dry_run=False,
    )

    (options, args) = E.start(parser,
                              argv=argv,
                              add_output_options=True)

    Storage.purge_run_id(options.run_id,
                         options.database_url,
                         dry_run=options.dry_run)

    E.stop()


if __name__ == "__main__":
    sys.exit(main())