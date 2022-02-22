public class User {

    private ScheduleMeeting scheduleMeeting;

    public void setScheduleMeeting(ScheduleMeeting scheduleMeeting) {
        this.scheduleMeeting = scheduleMeeting;
    }
    
    public void createScheduleMeeting() {
        this.scheduleMeeting.schedule();
    }
}
