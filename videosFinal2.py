
# ---- Khari Shiver ----
# ---- Homework #6 -----

import csv
import pprint

def get_video_data():
    """this function reads from a .csv file and converts the data into a list of dictionaries.
     each item in the list is a dictionary of a specific videos and their attributes."""

    vid_data = []
    with open('USvideos.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            if len(row) == 16:
                vid_dict = {'video_id': row[0],
                            'trending_date': row[1],
                            'title': row[2],
                            'channel_title': row[3],
                            'category_id': row[4],
                            'publish_times': row[5],
                            'tags': row[6],
                            'views': row[7],
                            'likes': row[8],
                            'dislikes': row[9],
                            'comment_count': row[10],
                            'thumbnail_link': row[11],
                            'comments_disabled': row[12],
                            'ratings_disabled': row[13],
                            'video_error': row[14],
                            'description': row[15]
                            }
                vid_data.append(vid_dict)
    return vid_data


def print_data(data):
    for entry in data:
        pprint.pprint(entry)

#create functions for the most and least popular channels
def most_pop(dictionary):
    return_dict = {'channel_title': None, 'num_total': 0}
    for k, v in dictionary.items():
        if int(v) > return_dict['num_total']:
            return_dict['channel_title'] = k
            return_dict['num_total'] = int(v)
    return return_dict


def least_pop(dictionary):
    return_dict = {'channel_title': None, 'num_total': float('Inf')}
    for k, v in dictionary.items():
        if int(v) < return_dict['num_total']:
            return_dict['channel_title'] = k
            return_dict['num_total'] = int(v)
    return return_dict


def get_most_popular_and_least_popular_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    #Creates dictionary to store output values.
    most_popular_and_least_popular_channel = {'most_popular_channel': None,
                                              'least_popular_channel': None,
                                              'most_pop_num_views': None,
                                              'least_pop_num_views': None}
    #Sums individual metrics for channels. 67 creates keys and a defalut value, 68 updates channel views
    sum_channel = {}
    for item in data[1:]:
        sum_channel.setdefault(item['channel_title'], 0)
        sum_channel[item['channel_title']] += int(item['views'])

    #Identifies the most popular channel based on most views. 72, 73 assign the value to the output dictionary.
    most_pop_dict = most_pop(sum_channel)
    most_popular_and_least_popular_channel['most_popular_channel'] = most_pop_dict['channel_title']
    most_popular_and_least_popular_channel['most_pop_num_views'] = most_pop_dict['num_total']

    #Identifies the leas popular channel based on fewest views. 77, 78 assign the value to the output dictionary.
    least_pop_dict = least_pop(sum_channel)
    most_popular_and_least_popular_channel['least_popular_channel'] = least_pop_dict['channel_title']
    most_popular_and_least_popular_channel['least_pop_num_views'] = least_pop_dict['num_total']

    return most_popular_and_least_popular_channel


def get_most_liked_and_disliked_channel(data):
    """ fill in the Nones for the dictionary below using the vid data """
    #Creates a dictionary to store the output values from the file.
    most_liked_and_disliked_channel = {'most_liked_channel': None,
                                       'num_likes': None,
                                       'most_disliked_channel': None,
                                       'num_dislikes': None}

    #Sums the total likes and dislikes per channel. Creates dictionaries to store values.
    # 97 creates keys, sets a default value for the likes dict, 98 updates total likes per channel.
    #99 creates keys and sets a default value for the dislikes dict. 100 updates total dislkes per channel.
    sum_channel_likes = {}
    sum_channel_dislikes = {}
    for item in data[1:]:
        sum_channel_likes.setdefault(item['channel_title'], 0)
        sum_channel_likes[item['channel_title']] += int(item['likes'])
        sum_channel_dislikes.setdefault(item['channel_title'], 0)
        sum_channel_dislikes[item['channel_title']] += int(item['dislikes'])

    #Identifies the most liked channel in dictionary and assigns the corresponding value to the output dictionary.
    liked_channel_dict = most_pop(sum_channel_likes)
    most_liked_and_disliked_channel['most_liked_channel'] = liked_channel_dict['channel_title']
    most_liked_and_disliked_channel['num_likes'] = liked_channel_dict['num_total']

    #Identifies the least liked channel in dictionary and assigns the corresponding value to the output dictionary.
    disliked_channel_dict = most_pop(sum_channel_dislikes)
    most_liked_and_disliked_channel['most_disliked_channel'] = disliked_channel_dict['channel_title']
    most_liked_and_disliked_channel['num_dislikes'] = disliked_channel_dict['num_total']

    return most_liked_and_disliked_channel


if __name__ == '__main__':
    vid_data = get_video_data()

    # uncomment the line below to see what the data looks like
    #print_data(vid_data)

    popularity_metrics = get_most_popular_and_least_popular_channel(vid_data)

    like_dislike_metrics = get_most_liked_and_disliked_channel(vid_data)

    print('Popularity Metrics: {}'.format(popularity_metrics))
    print('Like Dislike Metrics: {}'.format(like_dislike_metrics))