# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 10:00:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           90.91               33            0.65              6.69       1477.02                53.63         0.576            pass              0.706             68.1                           0.322                6.66              0.819                                 ok            True                  False
  DRAM           84.62               26            1.48              0.64         61.40                49.40         0.564            pass              0.386             33.2                           0.324               -4.50             -0.162                                 ok            True                  False
   BKR           91.30               23            1.20              0.48         57.17                33.54         0.511            pass              0.571             43.9                           0.324               -1.00             -0.255                                 ok            True                  False
  INTC           87.80               41            0.28              0.22        116.09                74.54         0.600            pass              0.611             47.6                           0.226               -6.45             -0.689 downtrend_blocked_slope_and_streak           False                  False
  META           84.62               39            0.26              1.35        741.32                55.50         0.588            pass              0.564             63.1                           0.401                0.46             -0.221                                 ok           False                  False
  QCOM           90.24               41            0.33              0.41        180.61                57.17         0.556            pass              0.707             59.4                           0.375               -9.11             -1.091 downtrend_blocked_slope_and_streak           False                  False
  ASML           83.33               36            0.40              5.26       1857.61                40.48         0.535            pass              0.451             45.1                           0.282                5.98              0.803                                 ok           False                  False
  LRCX           77.42               31            1.86              4.51        343.87                55.68         0.513            pass              0.253             20.5                           0.202                9.25              1.346                                 ok           False                  False
  ABNB           88.10               42            0.06              0.07        164.04                40.56         0.512            pass              0.739             90.7                           0.581                1.33              0.649                                 ok           False                  False
  TMUS           88.89               36            0.31              0.35        164.49                30.04         0.504            pass              0.657             65.5                           0.432                1.06             -0.063                                 ok           False                  False
  AMAT           83.78               37            1.48              5.63        539.87                48.32         0.482 below_threshold              0.405             25.2                           0.239               13.08              1.603                                 ok           False                  False
  MELI           82.61               46            0.10              1.35       1860.03                43.88         0.472 below_threshold              0.587             90.1                           0.527                1.76              0.047                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-06T10:00:02.462849-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T09:50:05.348208-04:00      manage_1000                    exit                                                                                                                                                                                                                                                {"asset_type": "option", "contract_symbol": "MRVL261120C00270000", "fill_price": 33.65, "pnl": 16560.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 37.63, "ticker": "MRVL"}
2026-10-06T00:00:06.226199-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 92, 'empty': 1}
2026-10-05T15:10:05.053706-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-05T15:05:06.249640-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-05T15:00:06.038960-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-05T14:55:02.074607-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-10-05T14:50:07.104378-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-05", "training_samples": 5905, "window": 5}
2026-10-05T14:50:07.104378-04:00       entry_1500                   entry {"allocated_cash": 44010.0, "asset_type": "option", "contract_symbol": "MRVL261120C00270000", "contracts": 18, "early_entry_score": 0.427, "entry_mode": "regular", "entry_option_price": 24.45, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2381.0, "option_spread_pct": 2.04, "option_volume": 509.0, "success_rate": 82.86, "ticker": "MRVL", "timing_score": 0.509}
2026-10-05T14:50:07.104378-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                     {"early_entry_score": 0.457, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 29.3, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TRI", "timing_score": 0.53}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006100002)

</details>
