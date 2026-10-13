# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 10:35:04 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           85.19               27            1.13              3.97        500.81                52.43         0.567            pass              0.481             57.5                           0.325               19.69              1.503                                 ok            True                  False
  MDLZ           93.75               16            0.67              0.29         61.67                19.83         0.555            pass              0.503             13.5                           0.206                4.38              0.648                                 ok            True                  False
  CSCO           91.67               24            0.71              0.57        115.09                34.19         0.537            pass              0.663             68.2                           0.391                7.50              0.916                                 ok            True                  False
  SHOP           82.86               35            0.85              1.06        178.76                48.43         0.516            pass              0.510             71.9                           0.568               19.86              2.068                                 ok            True                  False
  ISRG           90.00               10            2.14              6.39        424.90                25.00         0.506            pass              0.374             18.9                           0.335                1.53              0.526                                 ok            True                  False
  INTC           88.89               36            0.90              0.64        101.08                67.41         0.578            pass              0.681             70.9                           0.605              -13.36             -1.866 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.55               29            0.21              0.05         32.73                30.00         0.541            pass              0.800             73.1                           0.715                5.32              0.649                                 ok           False                  False
  MPWR           83.33               18            2.28             21.03       1310.22                51.39         0.540            pass              0.239             14.3                           0.159               -4.79             -0.373            downtrend_blocked_slope           False                  False
   CEG           88.64               44            0.07              0.15        293.83                56.17         0.510            pass              0.772             97.1                           0.759               11.00              1.676                                 ok           False                  False
  UPRO           85.71               35            0.37              0.41        155.29                28.94         0.509            pass              0.487             38.9                           0.298                4.68              0.590                                 ok           False                  False
  MCHP           95.83               24            1.52              0.78         73.49                37.42         0.494 below_threshold              0.659             38.8                           0.214               -7.71             -0.832            downtrend_blocked_slope           False                  False
   STX           85.00               20            3.48             18.37        745.38                70.16         0.494 below_threshold              0.429             59.8                           0.767              -20.41             -2.540            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-10-13T10:35:04.412949-04:00 early_entry_1035 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00 early_entry_1030 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:30:06.645428-04:00      manage_1030               exit  {"asset_type": "option", "contract_symbol": "CEG261120C00290000", "fill_price": 21.65, "pnl": 9300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.09, "ticker": "CEG"}
2026-10-13T10:25:06.600262-04:00 early_entry_1025 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:20:06.700982-04:00 early_entry_1020 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:15:06.623973-04:00 early_entry_1015 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:10:05.811238-04:00 early_entry_1010 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:05:05.477631-04:00 early_entry_1005 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T10:00:05.694425-04:00 early_entry_1000 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T09:50:04.590337-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "CTSH261120C00060000", "fill_price": 4.65, "pnl": 16000.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 27.4, "ticker": "CTSH"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013103504)

</details>
