# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:00:03 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$29,662.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$1,345.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-21                   2      4     12140.0                 13200.0        30.35           33.0      415.18        428.00     last_price_stale                        NaN                unavailable                   False          1060.0                   8.73         91.67               36              0.62         50.17            0.00                  40.33                2101.0          296.0               0.03                      ok
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14060.0         3.62            3.7      103.16        102.29          bid_ask_mid                        3.7                bid_ask_mid                    True           285.0                   2.07         94.74               19              0.93         28.13           35.16                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.00               20            0.80              0.57        102.86                33.02         0.605          pass              0.605             26.0                           0.207               -2.70             -0.246                      ok            True                  False
  MELI           90.00               20            2.03             23.68       1654.27                60.80         0.592          pass              0.481             29.4                           0.320                4.71              0.673                      ok            True                  False
  FTNT          100.00               41            0.62              0.58        133.68                66.43         0.585          pass              0.908             83.1                           0.755               15.29              1.650                      ok            True                   True
  ASML           88.57               35            0.58              6.59       1630.08                54.77         0.577          pass              0.584             43.7                           0.274                3.68              0.375                      ok            True                  False
   ADP          100.00               11            2.42              3.81        223.68                37.70         0.554          pass              0.474              3.9                           0.065                3.87              0.638                      ok            True                  False
  CTSH           85.71               21            1.48              0.55         52.52                46.65         0.541          pass              0.438             52.7                           0.656                6.27              1.323                      ok            True                  False
  ROST           92.59               27            0.90              1.48        234.18                38.50         0.529          pass              0.628             42.1                           0.353                8.46              0.752                      ok            True                  False
   ROP           91.30               23            1.25              2.87        325.71                26.18         0.503          pass              0.544             35.1                           0.412               -1.81              0.069                      ok            True                  False
  TEAM           91.30               46            0.14              0.08         85.38               109.49         0.690          pass              0.860             96.5                           0.871               -2.30              0.072                      ok           False                  False
  INTU           80.00               20            2.59              5.80        317.45                90.56         0.662          pass              0.210             25.6                           0.378              -20.76             -2.235 downtrend_blocked_slope           False                  False
  CSCO           83.33                6            1.98              1.67        119.69                52.25         0.656          pass              0.212             19.3                           0.148               19.55              1.878                      ok           False                  False
   TRI           73.33               15            1.53              0.92         85.47                55.00         0.610          pass              0.223             42.8                           0.325               -4.52              0.096                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                     detail
2026-05-26T10:00:03.313012-04:00 early_entry_1000 entry_skipped                           {"reason": "max_open_positions"}
2026-05-26T00:00:03.086607-04:00     data_refresh  data_refresh                                              {'saved': 92}
2026-05-25T23:55:01.101287-04:00   share_ext_2355 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:50:02.099383-04:00   share_ext_2350 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:45:01.097228-04:00   share_ext_2345 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:40:05.102217-04:00   share_ext_2340 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:35:01.093781-04:00   share_ext_2335 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:30:01.103317-04:00   share_ext_2330 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:25:02.099760-04:00   share_ext_2325 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:20:01.104241-04:00   share_ext_2320 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526100003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526100003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526100003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526100003)

</details>
