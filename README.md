# Content-Expiry-Notifier
The goal of the project is to develop a user-friendly desktop application that helps users manage items with expiry dates. The application notifies users about items nearing their expiry and allows them to track and organize their inventory effectively. It includes a secure login system to ensure only authorized users can access the application.

Key Features:
Secure Login System:

Provides a login page with username and password fields.
Access to the main functionality is restricted to authorized users.
Ensures data security and user-specific operations.

Content Management:

Allows users to add items with their respective expiry dates.
Stores item information in a structured format (item name and expiry date).
Enables tracking of expiry statuses dynamically.

Expiry Notification:

Automatically calculates the number of days left until an item's expiry.
Notifies users if an item is nearing expiry (e.g., within 3 days) or already expired.
Provides real-time updates on the status of all items in the inventory.

Graphical User Interface (GUI):

Intuitive interface designed using Python's tkinter library.
Organized into tabs:
Login Tab: For user authentication.
Content Notifier Tab: For managing and tracking items.
Includes a table view for displaying item details, expiry dates, and statuses.

User Feedback:

Alerts users with messages about nearing or expired items.
Provides success or error messages for actions like adding items or entering invalid data.
