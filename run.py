import argparse

from app import BANNER
from app.yamerge import from_sweet_potatoes_to_yams


def ym_parser():
    parser = argparse.ArgumentParser(description='Yammer Group Merge Utility')
    parser.add_argument('-dt', '--dev-token', type=str, help='Yammer Developer\'s Token', required=True)
    parser.add_argument('-mgid', '--master-group-id', type=int,
                        help='Group that contains the unique users that do not belong to the Slave Group',
                        required=True)
    parser.add_argument('-sgid', '--slave-group-id', type=int,
                        help='Group that will receive the unique users from the Master group', required=True)
    args = parser.parse_args()
    dt = args.dev_token
    mgid = args.master_group_id
    sgid = args.slave_group_id
    return dt, mgid, sgid


def main():
    dt, mgid, sgid = ym_parser()
    from_sweet_potatoes_to_yams(dt, mgid, sgid)


if __name__ == '__main__':
    print(BANNER)
    main()
