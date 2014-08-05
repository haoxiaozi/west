
horizontal_separator = "".center(80, "-")



# Source: http://stackoverflow.com/questions/695794/more-efficient-way-to-pickle-a-string

# def pickle(fname, obj):
#     import cPickle, gzip
#     cPickle.dump(obj=obj, file=gzip.open(fname, "wb", compresslevel=3), protocol=2)
#
# def unpickle(fname):
#     import cPickle, gzip
#     return cPickle.load(gzip.open(fname, "rb"))



def get_cochannel_and_first_adjacent(region, channel):
    affected_channels = [channel]
    for adj_chan in [channel-1, channel+1]:
        if channels_are_adjacent_in_frequency(region, adj_chan, channel):
            affected_channels.append(adj_chan)
    return affected_channels

def channels_are_adjacent_in_frequency(region, chan1, chan2):
    (low1, high1) = region.get_frequency_bounds(chan1)
    (low2, high2) = region.get_frequency_bounds(chan2)
    # If the channel is undefined for the region, we will return False
    if any([bound is None for bound in [low1, low2, high1, high2]]):
        return False
    return abs(low1 - high2) < .001 or abs(low2 - high1) < .001
