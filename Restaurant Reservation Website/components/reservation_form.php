<div class="reservation-page">
    <div class="container">
        <div class="reservation-main-content" id="link_main">
            <h2 class="section-title">Резервация столика</h2>
            <form class="reservation-form" action="###########" method="post">

                <div>
                <div>
                    <label for="fullname">Ваше имя и фамилия</label>
                    <input type="text" name="fullname" id="fullname" placeholder="Иван Иванов">
                </div>
                </div>

                <div class="reservation-form-general-info">
                <div>
                    <label>На сколько человек нужен столик?</label>
                    <input type="number" min="1" max="10" step="1" value="2" name="num_people" id="num_people">
                </div>
                
                <div>
                    <label>Впишите номер столика, который вы выбрали</label>
                    <input type="number" min="1" step="1" name="table_num" id="table_num">
                </div>
                </div>

                <div class="reservation-form-general-info">                
                <div>
                    <label>Во сколько вы придёте?</label>
                    <input type="datetime-local" id="reservation-time-start" name="reservation-time-start">
                </div>

                <div class="reservation-form-general-info">
                    <label>До скольки пробудете?</label>
                    <input type="datetime-local" id="reservation-time-start" name="reservation-time-start">
                </div>
                </div>

                <input type="submit" value="Забронировать">
            </form>
        </div>
    </div>
</div>