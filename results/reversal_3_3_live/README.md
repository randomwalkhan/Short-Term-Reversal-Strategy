# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 11:50:02 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$32,504.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$240.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14340.0        35.25          35.85      477.34        478.72          bid_ask_mid                      35.85                bid_ask_mid                    True           240.0                    1.7         97.22               36              0.69         45.69           47.97                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           93.10               29            0.50              0.79        224.29               139.09         0.779          pass              0.795             80.4                           0.455               20.04              3.766                                 ok            True                  False
  INTC           95.45               22            2.36              1.99        120.04                85.20         0.586          pass              0.574             11.8                           0.201                1.82              0.993                                 ok            True                  False
   TXN          100.00               14            1.83              4.04        314.22                35.59         0.526          pass              0.560             26.8                           0.418                0.65              0.477                                 ok            True                  False
  MDLZ           92.31               13            1.22              0.53         62.16                12.98         0.515          pass              0.543             47.6                           0.335                1.08              0.189                                 ok            True                  False
  NXPI           91.30               23            1.45              3.35        328.84                46.79         0.503          pass              0.579             46.8                           0.626               10.65              1.486                                 ok            True                  False
  INSM           69.70               33            1.38              1.05        107.92               111.11         0.763          pass              0.283             17.7                           0.340               -7.57             -0.392            downtrend_blocked_slope           False                  False
   AEP           77.78               18            0.40              0.36        127.61                25.60         0.589          pass              0.267             51.4                           0.458               -1.05              0.114                                 ok           False                  False
  REGN           87.88               33            0.68              2.97        620.25                44.05         0.545          pass              0.522             34.7                           0.248              -13.28             -1.070 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           90.00               10            1.93              5.28        387.87                41.30         0.539          pass              0.389             22.7                           0.306               -4.61             -0.340            downtrend_blocked_slope           False                  False
  GOOG           90.91               11            1.77              4.77        384.07                41.01         0.538          pass              0.437             28.4                           0.338               -4.50             -0.348            downtrend_blocked_slope           False                  False
  SBUX          100.00                6            1.81              1.28        100.20                16.60         0.527          pass              0.579             42.1                           0.244               -6.48             -0.751            downtrend_blocked_slope           False                  False
  AMGN           89.29               28            0.50              1.17        335.98                27.03         0.522          pass              0.573             51.2                           0.402                0.33              0.272                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-29T11:50:02.199680-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:25:01.209372-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:20:01.214678-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:15:06.204511-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:10:06.165530-04:00 early_entry_1110 entry_skipped {"reason": "daily_entry_limit"}
2026-05-29T11:05:07.175398-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529115002)

</details>
