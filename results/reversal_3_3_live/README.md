# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 14:35:05 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$18,164.25`
- Equity: `$32,644.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$380.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14480.0        35.25           36.2      477.34        474.27          bid_ask_mid                       36.2                bid_ask_mid                    True           380.0                    2.7         97.22               36              0.69         45.69           50.72                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           93.10               29            0.62              0.98        224.21               139.09         0.772            pass              0.784             77.0                           0.723               19.90              3.760                                 ok            True                  False
  MELI           94.44               36            0.61              7.22       1692.44                61.27         0.621            pass              0.721             33.5                           0.197                4.84              0.799                                 ok            True                  False
  INTC           95.45               22            2.30              1.95        120.06                85.20         0.582            pass              0.633             31.5                           0.544                1.88              0.996                                 ok            True                  False
  INSM           68.75               32            1.47              1.11        107.89               111.11         0.763            pass              0.261             12.6                           0.121               -7.65             -0.396            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.63              0.57        127.52                25.60         0.597            pass              0.148             22.9                           0.267               -1.28              0.103                                 ok           False                  False
  REGN           80.95               21            1.57              6.85        618.59                44.05         0.552            pass              0.175              6.9                           0.176              -14.06             -1.111 downtrend_blocked_slope_and_streak           False                  False
  KLAC           91.67               36            0.16              2.12       1926.72                52.36         0.547            pass              0.783             81.3                           0.619                1.80              0.913                                 ok           False                  False
 GOOGL           90.00               10            1.84              5.03        387.97                41.30         0.545            pass              0.400             26.3                           0.394               -4.52             -0.336            downtrend_blocked_slope           False                  False
  SBUX          100.00                7            1.62              1.14        100.26                16.60         0.533            pass              0.598             48.3                           0.450               -6.30             -0.742            downtrend_blocked_slope           False                  False
  GOOG           85.71               14            1.71              4.61        384.14                41.01         0.514            pass              0.323             30.8                           0.512               -4.44             -0.345            downtrend_blocked_slope           False                  False
  AMGN           91.18               34            0.27              0.65        336.20                27.03         0.498 below_threshold              0.727             73.0                           0.623                0.55              0.282                                 ok           False                  False
 CMCSA           85.71               14            1.33              0.23         25.06                17.83         0.497 below_threshold              0.268             13.0                           0.246               -1.37              0.065                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T12:00:03.057178-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529143505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529143505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529143505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529143505)

</details>
