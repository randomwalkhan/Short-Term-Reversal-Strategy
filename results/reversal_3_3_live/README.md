# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:35:01 EDT`
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

- Cash: `$32,694.50`
- Equity: `$32,694.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.76               29            2.78             17.14        874.13               110.38         0.567            pass              0.344             28.9                           0.347               -6.95              0.123                                 ok            True                  False
  GOOG           80.49               41            0.59              1.47        355.99                50.46         0.521            pass              0.364             32.8                           0.357               11.10              1.318                                 ok            True                  False
  INSM           66.67               18            2.58              2.40        131.52               110.04         0.726            pass              0.174             16.2                           0.212               20.77              1.471                                 ok           False                  False
  ALNY           86.11               36            0.88              1.33        215.55               128.30         0.623            pass              0.598             66.3                           0.563              -21.17             -3.061            downtrend_blocked_slope           False                  False
  INTC           85.00               40            0.29              0.20         99.72                86.24         0.605            pass              0.645             83.7                           0.565                7.80              1.459                                 ok           False                  False
  TMUS           88.57               35            0.49              0.62        179.71                57.01         0.603            pass              0.675             73.0                           0.765               -0.56             -0.130                                 ok           False                  False
   CSX           89.47               19            1.04              0.37         50.54                29.04         0.557            pass              0.422             18.0                           0.201               -5.74             -0.328 downtrend_blocked_slope_and_streak           False                  False
   MAR           93.10               29            0.77              1.95        358.84                38.09         0.525            pass              0.650             40.5                           0.238               -4.68             -0.862 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.92               39            0.68              1.72        357.01                51.28         0.520            pass              0.315             23.2                           0.277               11.12              1.347                                 ok           False                  False
  DRAM           76.00               25            4.12              1.48         50.80               108.98         0.519            pass              0.214             20.5                           0.309               -7.29              0.254                                 ok           False                  False
   PEP           81.82               33            0.08              0.08        138.41                22.07         0.504            pass              0.529             92.4                           0.778                1.24             -0.119                                 ok           False                  False
  PCAR           97.37               38            0.25              0.23        131.96                29.35         0.491 below_threshold              0.850             71.3                           0.372               -0.39             -0.137                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-07T10:35:01.485619-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:30:01.589091-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:25:02.606392-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "entry_ask": 3.7, "entry_bid": 2.95, "entry_mode": "early", "entry_option_price": 3.325, "hypothetical_budget": 16347.25, "hypothetical_contracts": 49, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 22.56, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.808, "shadow_only": true, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "matched_signals": 38, "recovery_stability_score": 0.808, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:20:01.443231-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:20:01.443231-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "INTC260918C00100000", "fill_price": 10.0575, "pnl": -1676.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "INTC"}
2026-08-07T10:15:06.143326-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:10:01.433730-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:05:05.478835-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow    {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807103501)

</details>
