<div class="restaurant-page">
    <div class="container">

        <div class="restaurant-main-content">
            <div class="restaurant-description">
                <h2 class="section-title"><?= $rest[0]['r_name'] ?></h2>
                <div class="restaurant-attributes">
                    <p class="restaurant-cuisine">Кухня: <?= $rest[0]['cuisine'] ?></p>
                    <p class="restaurant-rating">Рейтинг: <?= $rest[0]['rating'] ?></p>
                    <p class="restaurant-price">Цена: <?= $rest[0]['price_category'] ?></p>
                </div>
                <p><?= $rest[0]['description'] ?></p>
                <div class="restaurant-attributes">
                    <p class="restaurant-address">Адрес: <?= $rest[0]['address'] ?></p>
                </div>
                <div class="restaurant-attributes">
                    <p class="restaurant-timetable">Часы работы: <?= $rest[0]['opening_time'] ?> - <?= $rest[0]['closing_time'] ?></p>
                </div>
            </div>
            <img src="img/restaurant-photo.jpg" alt="Фото ресторана" class="restaurant-photo">
        </div>

        <div class="restaraunt-map">
            <h2 class="section-title">Карта ресторана</h2>
            <div class="restaraunt-map-img"><img src="img/restaurant-floor-plan.jpg" alt="Floor plan"></div>
        </div>
    </div>
</div>