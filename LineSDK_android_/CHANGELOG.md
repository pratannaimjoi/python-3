# Change Log

All notable changes to the LINE SDK will be documented in this file.

## 4.0.10 - 2018/11/29

* Fixed activity not found issue when using LINE App authentication.

## 4.0.8 - 2018/03/12

* Fixed an infinite loading indicator problem that occurs when the user attempts to log in before the LINE app has been opened for the first time.

## 4.0.7 - 2018/02/06

* Fixed a crash that occurs if the user exits the LINE app using the home button and then opens the SDK app before the LINE app finishes the authentication process.

## 4.0.6 - 2017/09/29

* Fixed an infinite loading indicator problem that occurs when the user presses the back button while the LINE app's passcode prompt is on screen.

## 4.0.5 - 2017/06/02

* Fixed an issue where a runtime error occurs upon calling startActivityForActivity with a login intent when using appcompat version 25.0.0 or higher.

## 4.0.4 - 2017/04/25

* Made a minor change to the SDK's authentication logic to fix a problem where onActivityResult does not get executed during app-to-app login.
* Fixed a known issue in 4.0.2 where onActivityResult returns a result of "CANCEL" on the first time that a user logs into an application using app-to-app login. 

## 4.0.2 - 2017/04/10

* Fixed an issue where browser login fails with an INTERNAL_ERROR on Android 4.x devices.

### Known Issues

* On 4.x devices, onActivityResult will return a result of "CANCEL" on the first time that a user logs into an application using app-to-app login. The user will be able to successfully log in from their second attempt. This issue is caused by a problem in the LINE Application and will be resolved in a future update.
* If the "Don't Keep Activities" developer option is set to ON, you may encounter unexpected issues during the login process. This is a known issue and will be fixed in a future update.

## 4.0.0 - 2017/01/24

* Initial Release
