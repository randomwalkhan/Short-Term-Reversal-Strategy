# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-11 09:49:51 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$15,257.25`
- Equity: `$29,309.75`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$-912.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CTSH     option         option CTSH260717C00055000       2026-06-09                   2     73     14965.0                 14052.5         2.05           1.92       52.68         51.12          bid_ask_mid                       1.92                bid_ask_mid                    True          -912.5                   -6.1         93.55               31              0.59         45.34           51.22                  51.28                1420.0           78.0                0.1                      ok
```

## Today's Closed Trades (2026-06-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               16            1.08              0.76        100.77                34.22         0.586          pass              0.663             54.8                           0.431                4.71              0.287                                 ok            True                  False
  WDAY           85.19               27            2.21              2.13        136.56                67.65         0.529          pass              0.430             41.8                           0.432                3.40             -0.464                                 ok            True                  False
   KDP           91.67               12            1.77              0.39         31.53                18.00         0.501          pass              0.508             44.6                           0.488                3.66              0.496                                 ok            True                  False
   ADP           96.88               32            0.81              1.31        230.54                32.69         0.500          pass              0.773             58.9                           0.509                4.26              0.308                                 ok            True                  False
    ZS           70.00               20            2.41              2.11        123.83               157.97         0.863          pass              0.266             37.7                           0.406               -6.40             -1.517 downtrend_blocked_slope_and_streak           False                  False
  INTU           77.78               27            1.57              3.13        282.88               101.53         0.732          pass              0.279             30.8                           0.286              -10.62             -1.717 downtrend_blocked_slope_and_streak           False                  False
   TRI           80.00               20            1.15              0.66         81.68                68.04         0.663          pass              0.295             53.9                           0.585               -4.11             -0.788 downtrend_blocked_slope_and_streak           False                  False
  CSCO           96.77               31            0.50              0.41        118.62                61.32         0.639          pass              0.827             74.3                           0.563               -0.36             -0.179                                 ok           False                  False
  TEAM           89.47               38            1.09              0.70         91.24                86.53         0.586          pass              0.708             70.1                           0.565               -2.95             -1.466 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               23            0.07              0.07        144.29                19.86         0.576          pass              0.806             87.2                           0.447               -0.38              0.084                                 ok           False                  False
  CTSH           86.96               23            1.33              0.48         51.60                46.99         0.552          pass              0.460             44.4                           0.405               -5.07             -0.790 downtrend_blocked_slope_and_streak           False                  False
  MSFT           54.55               11            1.72              4.79        395.31                36.94         0.543          pass              0.131             23.4                           0.240               -8.54             -1.370 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-06-11T05:50:04.507646-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:45:04.534672-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:43:14.603904-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:25:01.583807-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:20:01.619276-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:15:03.611624-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:10:01.640984-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:05:01.109069-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T05:00:02.624935-04:00 data_refresh data_refresh {'saved': 93}
2026-06-11T04:55:01.092437-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260611094951)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260611094951)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260611094951)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260611094951)

</details>
