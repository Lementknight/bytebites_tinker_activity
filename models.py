"""
ByteBites Backend Models
Implements core classes for managing customers, food items, menus, and transactions.
"""

from typing import List


class Customer:
    """
    Represents a ByteBites user with identification and purchase tracking for verification.
    """
    
    def __init__(self, name: str) -> None:
        """
        Initialize a Customer with a name and empty purchase history.
        
        Args:
            name (str): The customer's name
        """
        self.name: str = name
        self.purchaseHistory: List['Transaction'] = []
    
    def verifyUser(self) -> bool:
        """
        Verify if the customer is a valid/registered user.
        
        Returns:
            bool: True if customer has a name, False otherwise
        """
        return self.name is not None and len(self.name) > 0


class FoodItem:
    """
    Represents a single food product available for purchase with browsable attributes and ratings.
    """
    
    def __init__(self, name: str, price: float, category: str, popularityRating: float) -> None:
        """
        Initialize a FoodItem with product details.
        
        Args:
            name (str): The item's name (e.g., "Spicy Burger")
            price (float): The cost of the item
            category (str): The category classification (e.g., "Drinks", "Desserts")
            popularityRating (float): A rating indicating how popular the item is
        """
        self.name: str = name
        self.price: float = price
        self.category: str = category
        self.popularityRating: float = popularityRating


class Menu:
    """
    Central inventory that manages and provides access to all food items with filtering capabilities.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty Menu with no items.
        """
        self.items: List[FoodItem] = []
    
    def addItem(self, item: FoodItem) -> None:
        """
        Add a new FoodItem to the menu.
        
        Args:
            item (FoodItem): The food item to add
        """
        self.items.append(item)
    
    def filterByCategory(self, category: str) -> List[FoodItem]:
        """
        Return a filtered list of FoodItems matching the specified category.
        
        Args:
            category (str): The category to filter by (e.g., "Drinks", "Desserts")
        
        Returns:
            list: A list of FoodItems in the specified category
        """
        return [item for item in self.items if item.category == category]
    
    def getAllItems(self) -> List[FoodItem]:
        """
        Return the complete list of all available items.
        
        Returns:
            list: All FoodItems in the menu
        """
        return self.items


class Transaction:
    """
    Represents a purchase session that groups selected items and calculates total cost.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty Transaction with no selected items and zero total cost.
        """
        self.selectedItems: List[FoodItem] = []
        self.totalCost: float = 0.0
    
    def addItem(self, item: FoodItem) -> None:
        """
        Add a FoodItem to the transaction.
        
        Args:
            item (FoodItem): The food item to add to this transaction
        """
        self.selectedItems.append(item)
        self.totalCost += item.price
    
    def computeTotal(self) -> float:
        """
        Calculate and return the sum of all selected items' prices.
        
        Returns:
            float: The total cost of all items in the transaction
        """
        return sum(item.price for item in self.selectedItems)
    
    def getItems(self) -> List[FoodItem]:
        """
        Return the list of selected items.
        
        Returns:
            list: All FoodItems in this transaction
        """
        return self.selectedItems
