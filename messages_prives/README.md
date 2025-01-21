# Messages Privés  

## API gestion des messages  

- **Description :**  
  API permettant la gestion des messages privés entre utilisateurs. Elle inclut l'envoi, la récupération, la suppression et la mise à jour des messages.  

---

### **1. Envoyer un message privé**  
- **Description :**  
  Permet à un utilisateur d'envoyer un message privé à un autre utilisateur.  

#### **Requête client**  
- **URL :**  
  ```yaml
  messages
  ```  
- **Méthode :**  
  ```yaml
  POST
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  
- **Body :**  
  ```yaml
  { 
      sender: "user1",
      receiver: "user2",
      content: "Bonjour, comment ça va ?"
  }
  ```  

#### **Réponse serveur**  
- **Code de réponse :**  
  ```yaml
  201 : Message envoyé avec succès
  400 : Requête invalide (paramètres manquants ou incorrects)
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  
- **Body :**  
  ```yaml
  { 
      messageId: "12345",
      status: "Message envoyé avec succès"
  }
  ```  

---

### **2. Récupérer les messages entre deux utilisateurs**  
- **Description :**  
  Permet de récupérer tous les messages échangés entre deux utilisateurs.  

#### **Requête client**  
- **URL :**  
  ```yaml
  messages/{user1}/{user2}
  ```  
- **Méthode :**  
  ```yaml
  GET
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  

#### **Réponse serveur**  
- **Code de réponse :**  
  ```yaml
  200 : Liste des messages récupérée avec succès
  404 : Aucun message trouvé
  400 : Requête invalide
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  
- **Body :**  
  ```yaml
  [
      {
          messageId: "12345",
          sender: "user1",
          receiver: "user2",
          content: "Bonjour, comment ça va ?",
          timestamp: "2025-01-19T14:30:00Z",
          isRead: false
      },
      {
          messageId: "12346",
          sender: "user2",
          receiver: "user1",
          content: "Je vais bien, merci !",
          timestamp: "2025-01-19T14:35:00Z",
          isRead: true
      }
  ]
  ```  

---

### **3. Marquer un message comme lu**  
- **Description :**  
  Permet de mettre à jour l'état d'un message pour indiquer qu'il a été lu.  

#### **Requête client**  
- **URL :**  
  ```yaml
  messages/{message_id}
  ```  
- **Méthode :**  
  ```yaml
  PUT
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  

#### **Réponse serveur**  
- **Code de réponse :**  
  ```yaml
  200 : Message marqué comme lu avec succès
  404 : Message introuvable
  400 : Requête invalide
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  
- **Body :**  
  ```yaml
  { 
      messageId: "12345",
      status: "Message marqué comme lu avec succès"
  }
  ```  

---

### **4. Supprimer un message**  
- **Description :**  
  Permet à un utilisateur de supprimer un message.  

#### **Requête client**  
- **URL :**  
  ```yaml
  messages/{message_id}
  ```  
- **Méthode :**  
  ```yaml
  DELETE
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  

#### **Réponse serveur**  
- **Code de réponse :**  
  ```yaml
  200 : Message supprimé avec succès
  404 : Message introuvable
  400 : Requête invalide
  ```  
- **Content-Type :**  
  ```yaml
  application/json
  ```  
- **Body :**  
  ```yaml
  { 
      messageId: "12345",
      status: "Message supprimé avec succès"
  }
  ```  

### Template 
 - Description : (...)
##### Réquête client
- URL :
``` messages/... ```      
- Méthode : ```POST - GET - DELETE - ...```
- Content-Type : ``` ... ```
- Body : 
    ```yaml 
    { 
        param1: ...
        param2: ...
    }
    ```      
##### Réponse serveur
- Code de réponse : 
    ```yaml 
    200 : OK
    404 : ...
    400 : ...
    ...
    ```    
- Content-Type : ``` ... ```
- Body : 
    ```yaml 
        { 
            ...
        }
    ``` 