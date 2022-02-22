public class App {
    public static void main(String[] args) throws Exception {
        
        User user = new User();

        user.setScheduleMeeting(new LimitedMeeting());
        user.createScheduleMeeting();

        System.out.println("--------------------------------");

        user.setScheduleMeeting(new UnlimitedMeeting());
        user.createScheduleMeeting();
    }
}
