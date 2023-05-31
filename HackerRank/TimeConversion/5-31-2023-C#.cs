  public static string timeConversion(string s)
  {
      // Time Complexity:  O(1)
      // Space Complexity: O(1)

      // Time is in hh:mm:ssAM or hh:mm:ssPM format
      // 8 should retrieve everything but the last two characters
      string convertedTime = s.Substring(0, 8);

      // Hour of the current time to be converted to 24 hour format
      int hour = 0;

      // Attempts to convert string hour into int hour, if fail
      // return nothing
      if (!Int32.TryParse(convertedTime.Substring(0, 2), out hour)) {
          Console.WriteLine("Not parsable\n");
          return "";
      }

      // If the last two characters are PM
      if (s.Substring(8) == "PM") {
          if (hour != 12) {
              hour += 12;
          }
      // IF the last two characters are AM
      } else {
          if (hour == 12) {
              hour = 0;
          }
      }

      // Changes hour in convertedTiem to adjustHours
      if (hour > 9) {
          convertedTime = hour.ToString() + convertedTime.Substring(2);
      // Changes hour in convertedTiem to adjustHours, adds spacing
      } else {
          convertedTime = "0" + hour.ToString() + convertedTime.Substring(2);
      }


      return convertedTime;
  }
