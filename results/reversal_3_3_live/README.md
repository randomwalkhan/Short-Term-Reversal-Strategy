# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 15:55:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$38,003.30`
- Equity: `$73,203.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$-350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00160000       2026-09-25                   0     20     35550.0                 35200.0        17.77           17.6      158.68        158.54          bid_ask_mid                       17.6                bid_ask_mid                    True          -350.0                  -0.98          93.1               29              1.81         73.26           73.39                 109.71                2435.0         2824.0               0.01                      ok
```

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.80              2.04        160.74               109.71         0.712          pass              0.666             39.7                           0.311               21.17              2.821                                 ok            True                  False
  FTNT           83.33               12            2.97              3.72        177.08                58.17         0.561          pass              0.186              9.1                           0.278                9.13              1.043                                 ok            True                  False
   TRI           86.67               30            1.27              0.89         99.94                57.78         0.555          pass              0.588             73.9                           0.753                3.49             -0.128                                 ok            True                  False
  WDAY           93.75               32            0.92              1.22        190.47                49.78         0.533          pass              0.777             70.1                           0.446                2.24              0.218                                 ok            True                  False
  TEAM          100.00               23            2.69              3.63        191.05                57.21         0.521          pass              0.539              0.0                           0.150                4.37              0.543                                 ok            True                  False
  SHOP           80.95               21            2.21              2.24        144.20                62.63         0.516          pass              0.223             24.2                           0.226               10.22              1.283                                 ok            True                  False
  CRWD           77.78               18            3.03              5.52        257.31                96.70         0.680          pass              0.121              0.0                           0.209               20.55              2.013                                 ok           False                  False
  PANW           55.56                9            4.01             10.94        385.23                80.20         0.580          pass              0.061              1.1                           0.158               10.58              1.148                                 ok           False                  False
   KHC           92.86               14            1.07              0.18         23.78                23.05         0.536          pass              0.522             32.9                           0.506               -3.22             -0.352            downtrend_blocked_slope           False                  False
  ADSK           79.41               34            0.97              1.43        210.74                55.76         0.514          pass              0.211              0.0                           0.191               -1.09             -0.288                                 ok           False                  False
  META           75.00                8            3.08             16.78        770.40                47.68         0.513          pass              0.120             22.8                           0.558               16.39              1.786                                 ok           False                  False
  NFLX           78.12               32            0.84              0.42         71.54                37.57         0.506          pass              0.254             18.9                           0.226               -8.11             -1.163 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-09-25T15:10:05.947782-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:05:07.061521-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:00:05.968673-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:55:06.191609-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:50:06.559632-04:00       entry_1500              entry {"allocated_cash": 35550.0, "asset_type": "option", "contract_symbol": "MSTR261120C00160000", "contracts": 20, "early_entry_score": 0.665, "entry_mode": "regular", "entry_option_price": 17.775, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 2435.0, "option_spread_pct": 1.41, "option_volume": 2824.0, "success_rate": 93.1, "ticker": "MSTR", "timing_score": 0.711}
2026-09-25T14:50:06.559632-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-25", "training_samples": 5827, "window": 5}
2026-09-25T12:00:04.925096-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:55:06.011160-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:50:06.515187-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:45:06.706431-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925155506)

</details>
