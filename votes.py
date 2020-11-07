def getVotesNeeded(percentReported, leadingCount, trailingCount):
    votesSoFar = leadingCount + trailingCount
    votesLeft = int((votesSoFar / (percentReported / 100)) - votesSoFar)
    netVotesNeeded = (leadingCount - trailingCount)

    if netVotesNeeded > votesLeft:
        return "it is impossible for Trump to win."

    netPercentageNeeded = (netVotesNeeded / votesLeft) * 100
    percentageNeeded = round((netPercentageNeeded / 2) + 50, 2)
    message = str(votesSoFar) + " votes have been cast so far.\n" + str(votesLeft) + " votes remain.\n" + "Trump is trailing by " + str(netVotesNeeded) + " votes.\n" + "He needs " + str(percentageNeeded) + "% of the remaing votes to tie the race.\n"
    return message

if __name__ == '__main__':
    percentReported = int(input('Enter percent reported as a number between 0 and 100: '))
    bidenCount = int(input('Enter vote count for Biden: '))
    trumpCount = int(input('Enter vote count for Trump: '))
    print(getVotesNeeded(percentReported, bidenCount, trumpCount))