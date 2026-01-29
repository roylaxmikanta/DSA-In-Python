class Meeting:
    def maximumMeetings(self,start,end):
        meet=[(start[i],end[i],i+1) for i in range(len(start))]
        meet.sort(key=lambda x:(x[1],x[0]))
        count=1
        last_time=meet[0][1]
        for i in range(1,len(start)):
            if(meet[i][0]>last_time):
                count+=1
                last_time=meet[i][1]
        return count
        
m=Meeting()
print(m.maximumMeetings([1, 3, 0, 5, 8, 5],[2, 4, 6, 7, 9, 9]))

#time complexity : o(N)
#space complexity : o(N)