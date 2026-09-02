# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-02 15:00:06 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$1,008.10`
- Equity: `$48,338.10`
- Realized PnL: `$37,718.10`
- Unrealized PnL: `$620.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CPRT     option         option CPRT261016C00032500       2026-09-01                   1    144     23760.0                 24480.0         1.65           1.70       32.33         32.29          bid_ask_mid                       1.70                bid_ask_mid                    True           720.0                   3.03          87.5               16              1.99         38.72           41.75                  40.13                 398.0          105.0               0.06                      ok
  MSTR     option         option MSTR261009C00122000       2026-09-02                   0     20     22950.0                 22850.0        11.48          11.42      122.50        122.54          bid_ask_mid                      11.42                bid_ask_mid                    True          -100.0                  -0.44          80.0               30              1.91         71.34           70.76                  86.77                 141.0           20.0               0.07                      ok
```

## Today's Closed Trades (2026-09-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            1.88              1.64        124.18                86.77         0.591          pass              0.307             38.3                           0.268               17.54              1.555                                 ok            True                  False
  COST           90.91               11            1.35              8.88        936.16                19.36         0.551          pass              0.353              0.0                           0.198               -3.10             -0.203                                 ok            True                  False
    ZS          100.00               18            3.02              3.77        176.76                60.79         0.521          pass              0.577             23.7                           0.253               -6.29              0.052                                 ok            True                  False
  PAYX          100.00               20            0.90              0.79        125.30                25.34         0.510          pass              0.698             60.2                           0.677                1.64              0.241                                 ok            True                  False
  MNST           77.78                9            1.74              0.55         44.75               424.41         1.000          pass              0.100              0.0                           0.159               -6.80             -0.742            downtrend_blocked_slope           False                  False
   WDC           82.35               34            0.54              1.71        449.71                82.26         0.653          pass              0.532             81.2                           0.716               -3.05             -0.221           downtrend_blocked_streak           False                  False
  MRVL           79.41               34            1.34              1.97        209.55                79.24         0.592          pass              0.397             59.1                           0.668              -12.52             -1.658 downtrend_blocked_slope_and_streak           False                  False
   STX           86.67               30            1.37              7.85        813.28                70.47         0.580          pass              0.561             63.8                           0.640               -3.26             -0.261 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               14            1.25              0.43         48.57                20.15         0.531          pass              0.614             44.9                           0.453               -6.41             -0.586 downtrend_blocked_slope_and_streak           False                  False
  LRCX           82.35               34            0.93              1.88        289.39                48.78         0.512          pass              0.435             53.7                           0.507               -6.40             -0.696 downtrend_blocked_slope_and_streak           False                  False
  CSCO           89.74               39            0.45              0.34        109.59                36.37         0.509          pass              0.694             63.5                           0.681               -1.18             -0.059                                 ok           False                  False
  MPWR           84.21               38            0.18              1.52       1225.31                40.84         0.508          pass              0.609             86.4                           0.459               -5.87             -0.657            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-02T15:00:06.384646-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-02T14:58:03.772540-04:00       entry_1500              entry {"allocated_cash": 22950.0, "asset_type": "option", "contract_symbol": "MSTR261009C00122000", "contracts": 20, "early_entry_score": 0.304, "entry_mode": "regular", "entry_option_price": 11.475, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 141.0, "option_spread_pct": 6.54, "option_volume": 20.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.589}
2026-09-02T14:58:03.772540-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-02", "training_samples": 5758, "window": 5}
2026-09-02T12:00:02.480923-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:55:01.504562-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:50:01.337983-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:45:01.308184-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:40:01.399320-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:35:06.484785-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-02T11:30:01.496570-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260902150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260902150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260902150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260902150006)

</details>
