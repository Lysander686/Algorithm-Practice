- sign in

        mutation {
        signIn(
            username: "BeeBoop",
            email: "robot@example.com",
            password: "NotARobot10010!"  )
        }


        db.notes.find({_id: ObjectId("5ffd08192d60702cecf1021b")})