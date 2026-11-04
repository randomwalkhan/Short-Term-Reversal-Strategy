# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 09:35:06 EST`
Last processed slot: `manage_0930`

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
  INTC           65.00               20            3.12              1.32         59.98               129.60         0.748            pass              0.218             25.6                           0.346              -36.90             -4.957            downtrend_blocked_slope           False                  False
  FTNT           88.46               26            1.72              1.54        127.45                91.30         0.678            pass              0.489             29.6                           0.322              -27.66             -4.333 downtrend_blocked_slope_and_streak           False                  False
  SOXL           65.00               20            6.16              3.16         71.89               167.58         0.550            pass              0.195             24.4                           0.338              -33.43             -3.107            downtrend_blocked_slope           False                  False
   BKR           77.78                9            2.44              0.90         52.40                46.45         0.544            pass              0.089             11.6                           0.221               -8.04             -0.676            downtrend_blocked_slope           False                  False
  DRAM           61.11               18            3.08              1.03         47.23                69.30         0.532            pass              0.159             17.4                           0.237               -6.02             -0.163                                 ok           False                  False
    ZS           90.00               30            1.65              2.60        223.98                64.45         0.530            pass              0.531             25.8                           0.342               -4.30             -0.966 downtrend_blocked_slope_and_streak           False                  False
  AVGO           72.00               25            1.32              3.08        330.81                44.04         0.517            pass              0.251             33.1                           0.351               -2.98             -0.044                                 ok           False                  False
  ASML           71.43                7            2.93             31.82       1538.50                44.05         0.515            pass              0.078              8.8                           0.314              -10.02             -0.576            downtrend_blocked_slope           False                  False
  TEAM           96.88               32            1.40              1.88        190.25                53.65         0.496 below_threshold              0.763             55.7                           0.379              -16.47             -2.262            downtrend_blocked_slope           False                  False
   ADI           87.50               24            1.26              3.69        418.21                38.61         0.493 below_threshold              0.412             23.0                           0.291                2.11              0.607                                 ok           False                  False
  LRCX           66.67               30            1.75              2.83        229.51                62.98         0.493 below_threshold              0.311             42.8                           0.383              -13.09             -0.597            downtrend_blocked_slope           False                  False
  SNPS           74.29               35            0.67              2.16        461.95                45.79         0.490 below_threshold              0.344             42.7                           0.388                1.91              0.719                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:05:04.979432-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:00:05.978517-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:55:04.978613-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:50:06.793337-05:00       entry_1500              entry {"allocated_cash": 68150.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "contracts": 470, "early_entry_score": 0.508, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 1121.0, "option_spread_pct": 6.9, "option_volume": 33.0, "success_rate": 90.91, "ticker": "MDLZ", "timing_score": 0.603}
2026-11-03T14:50:06.793337-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-03", "training_samples": 6256, "window": 5}
2026-11-03T12:00:06.009720-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:55:04.283382-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104093506)

</details>
