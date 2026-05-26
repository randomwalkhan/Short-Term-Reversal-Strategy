# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 09:45:02 EDT`
Last processed slot: `manual`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$2,402.75`
- Equity: `$28,552.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$235.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14250.0         3.62           3.75      103.16         103.0     last_price_stale                        NaN                unavailable                   False           475.0                   3.45         94.74               19              0.93         28.13            1.56                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   2      4     12140.0                 11900.0        30.35          29.75      415.18         427.8     last_price_stale                        NaN                unavailable                   False          -240.0                  -1.98         91.67               36              0.62         50.17            0.00                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               36            1.74              1.04         84.97               109.49         0.652          pass              0.645             56.4                           0.471               -3.87             -0.001                      ok            True                  False
  CSCO           87.50               16            1.35              1.14        119.92                52.25         0.633          pass              0.438             44.9                           0.284               20.32              1.907                      ok            True                  False
  FTNT          100.00               30            1.25              1.17        133.43                66.43         0.621          pass              0.794             66.1                           0.505               14.57              1.621                      ok            True                  False
  MELI           88.89               18            2.29             26.70       1652.98                60.80         0.587          pass              0.410             20.4                           0.235                4.43              0.661                      ok            True                  False
   ADP          100.00               14            2.12              3.35        223.88                37.70         0.551          pass              0.529             15.7                           0.234                4.19              0.652                      ok            True                  False
  CTSH           82.35               17            1.82              0.67         52.46                46.65         0.542          pass              0.289             41.8                           0.447                5.90              1.307                      ok            True                  False
  ROST           93.75               32            0.70              1.15        234.32                38.50         0.509          pass              0.729             54.9                           0.320                8.68              0.761                      ok            True                  False
  QCOM           92.86               42            0.08              0.14        238.10               100.82         0.679          pass              0.764             51.0                           0.260                0.18              0.459                      ok           False                  False
  INTU           81.25               16            3.03              6.79        317.03                90.56         0.661          pass              0.178             12.9                           0.239              -21.12             -2.256 downtrend_blocked_slope           False                  False
   TRI           73.33               15            1.58              0.95         85.45                55.00         0.613          pass              0.173             26.0                           0.283               -4.57              0.094                      ok           False                  False
  ASML           89.74               39            0.13              1.51       1632.25                54.77         0.580          pass              0.772             87.1                           0.455                4.15              0.395                      ok           False                  False
  GEHC           76.74               43            0.12              0.05         64.21                59.75         0.573          pass              0.526             89.7                           0.569                3.98              0.452                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                     detail
2026-05-26T00:00:03.086607-04:00   data_refresh  data_refresh                                              {'saved': 92}
2026-05-25T23:55:01.101287-04:00 share_ext_2355 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:50:02.099383-04:00 share_ext_2350 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:45:01.097228-04:00 share_ext_2345 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:40:05.102217-04:00 share_ext_2340 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:35:01.093781-04:00 share_ext_2335 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:30:01.103317-04:00 share_ext_2330 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:25:02.099760-04:00 share_ext_2325 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:20:01.104241-04:00 share_ext_2320 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:15:05.147623-04:00 share_ext_2315 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526094502)

</details>
