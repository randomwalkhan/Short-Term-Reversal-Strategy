# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 11:30:01 EST`
Last processed slot: `manage_1130`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           54.55               11            4.89              2.07         59.66               129.60         0.678            pass              0.140             21.7                           0.369              -38.05             -5.041            downtrend_blocked_slope           False                  False
  FTNT           91.11               45            0.22              0.20        128.03                91.30         0.660            pass              0.835             91.1                           0.420              -26.56             -4.264 downtrend_blocked_slope_and_streak           False                  False
  REGN           70.59               17            1.58             10.73        968.76                48.26         0.532            pass              0.256             52.2                           0.516               18.91              2.154                                 ok           False                  False
    ZS           90.00               30            1.56              2.46        224.04                64.45         0.531            pass              0.543             29.9                           0.197               -4.21             -0.962 downtrend_blocked_slope_and_streak           False                  False
  AVGO           66.67               18            1.88              4.37        330.26                44.04         0.509            pass              0.224             39.8                           0.500               -3.53             -0.070                                 ok           False                  False
  TEAM           95.24               21            2.13              2.85        189.83                53.65         0.499 below_threshold              0.621             32.6                           0.183              -17.09             -2.295            downtrend_blocked_slope           False                  False
  SNPS           66.67               24            1.44              4.67        460.88                45.79         0.489 below_threshold              0.263             40.4                           0.330                1.11              0.683                                 ok           False                  False
  CSCO           81.48               27            0.81              0.58        102.72                32.31         0.486 below_threshold              0.289             29.1                           0.160               -4.77             -0.538 downtrend_blocked_slope_and_streak           False                  False
  CRWD           80.00               25            1.91              3.28        243.28                59.77         0.485 below_threshold              0.261             37.3                           0.229                0.28             -0.163                                 ok           False                  False
  NVDA           66.67               12            2.10              3.03        205.39                32.59         0.483 below_threshold              0.136             24.7                           0.270               -8.83             -0.750 downtrend_blocked_slope_and_streak           False                  False
  PANW           80.95               42            0.47              1.14        349.71                58.95         0.482 below_threshold              0.518             81.3                           0.380                0.38             -0.414                                 ok           False                  False
   TXN           90.00               30            0.69              1.51        311.84                35.19         0.481 below_threshold              0.673             75.0                           0.671                9.56              1.050                                 ok           False                   True
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-04T11:30:01.206100-05:00 early_entry_1130 early_entry_shadow {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "entry_ask": 9.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.025, "hypothetical_budget": 64815.78, "hypothetical_contracts": 71, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 11.63, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "matched_signals": 30, "recovery_stability_score": 0.671, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:25:01.112223-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:10:06.095882-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:05:05.102696-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:00:06.142826-05:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:55:05.872153-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:50:01.073717-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:45:06.080756-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104113001)

</details>
