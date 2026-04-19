select category, sum(amt)
from credit_card_transactions
group by 1
order by 2 desc;

select cc_num, sum(amt)
from credit_card_transactions
where trans_date_trans_time between '2019-05-01' and '2020-05-01'
group by cc_num
order by 2 desc;

select trans_num, amt
from credit_card_transactions
order by 2 desc
limit 5;


select date_trunc('month', date(trans_date_trans_time)),category, sum(amt)
from credit_card_transactions
group by 1,2
order by 1 desc;