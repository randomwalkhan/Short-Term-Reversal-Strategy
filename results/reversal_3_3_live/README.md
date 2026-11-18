# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 10:59:10 EST`
Last processed slot: `manage_1100`

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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               44            0.70              1.96        398.10               121.47         0.765          pass              0.755             62.4                           0.576               45.77              2.280                       ok            True                   True
   TXN           93.75               32            0.60              1.25        295.33                59.80         0.598          pass              0.772             66.4                           0.540               -5.59              0.207                       ok            True                  False
  MDLZ           95.00               20            0.58              0.27         66.63                29.89         0.587          pass              0.707             60.6                           0.689               -1.51              0.019                       ok            True                  False
 CMCSA           91.67               24            0.67              0.12         25.26                34.73         0.568          pass              0.602             46.9                           0.386                1.17              0.286                       ok            True                  False
   CEG           92.11               38            0.59              1.11        267.59                61.66         0.550          pass              0.787             74.0                           0.571                8.61              1.156                       ok            True                   True
   ADP           88.00               25            0.71              1.53        307.63                28.72         0.547          pass              0.494             42.1                           0.308                0.84              0.195                       ok            True                  False
  COST           86.36               22            0.71              5.54       1107.71                22.66         0.542          pass              0.415             37.1                           0.314                5.32              0.625                       ok            True                  False
   WMT           85.00               20            0.93              0.83        127.16                25.55         0.539          pass              0.408             51.4                           0.357               -2.20             -0.005                       ok            True                  False
  META           83.87               31            0.75              3.26        617.47                41.87         0.534          pass              0.412             38.4                           0.305               -2.51              0.014                       ok            True                  False
  GILD           88.46               26            1.04              1.24        169.73                31.94         0.508          pass              0.500             39.0                           0.321               -3.43             -0.119                       ok            True                  False
   LIN           85.00               20            1.00              3.62        513.56                18.95         0.503          pass              0.332             27.4                           0.389               -2.82             -0.109                       ok            True                  False
  INTC           71.88               32            1.63              0.63         54.90               143.31         0.816          pass              0.372             48.0                           0.354               -6.86             -0.109 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-18T10:59:10.549422-05:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CEG261224C00265000", "current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "entry_ask": 19.0, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 52959.4, "hypothetical_contracts": 30, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 18.39, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "matched_signals": 38, "recovery_stability_score": 0.571, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.755, "early_reclaim_pct": 62.4, "matched_signals": 44, "recovery_stability_score": 0.576, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.765, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-18T10:59:10.549422-05:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "APP261218C00400000", "fill_price": 28.17, "pnl": -5321.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-18T00:00:06.344355-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T14:50:06.628486-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 53210.0, "asset_type": "option", "contract_symbol": "APP261218C00400000", "contracts": 17, "early_entry_score": 0.66, "entry_mode": "regular", "entry_option_price": 31.3, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 1252.0, "option_spread_pct": 1.28, "option_volume": 197.0, "success_rate": 94.12, "ticker": "APP", "timing_score": 0.778}
2026-11-17T14:50:06.628486-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-17", "training_samples": 6239, "window": 5}
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118105910)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118105910)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118105910)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118105910)

</details>
