<div class="restaurants">
      <div class="container">
        <div class="restaurant-list">
            <h2 class="section-title">Рестораны</h2>

            <?php for ($i=0; $i<$rnum; $i++): ?>
                <dl>
                <div class="restaurant-desc">
                    <dt>
                        <h3 class="restaurant-name"><?= $rest[$i]['r_name'] ?></h3>
                        <div class="restaurant-attributes">
                            <p class="restaurant-cuisine">Кухня: <?= $rest[$i]['cuisine'] ?></p>
                            <p class="restaurant-rating">Peйтинг: <?= $rest[$i]['rating'] ?></p>
                            <p class="restaurant-price">Цена: <?= $rest[$i]['price_category'] ?></p>
                        </div>
                    </dt>
                    <dd>
                        <p> <?= $rest[$i]['description'] ?> </p>
                    </dd>
                </div>

                <div class="restaurant-btn">
                    <a href="restaurant.php?id=<?= $rest[$i]['id_restaurant'] ?>">Подробнее</a>
                    <a href="restaurant.php#link_main">Забронировать</a>
                </div>
            </dl>
            <?php endfor; ?>


            


        </div>
      </div>
    </div>