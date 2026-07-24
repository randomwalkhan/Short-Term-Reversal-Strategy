# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 10:10:05 EDT`
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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           83.33               24            0.98              0.38         55.84                61.86         0.661          pass              0.438             63.3                           0.314               19.71              1.850                                 ok            True                  False
   STX           85.71               21            2.96             18.94        905.24               102.76         0.646          pass              0.416             42.0                           0.433               -2.64              0.387                                 ok            True                  False
   WDC           90.00               20            4.51             17.63        550.74               114.14         0.591          pass              0.453             20.3                           0.243               -8.49             -0.260                                 ok            True                  False
  GILD           91.30               23            0.83              0.76        130.53                35.55         0.569          pass              0.473              9.2                           0.122               -0.04             -0.051                                 ok            True                  False
  ASML           93.10               29            1.56             19.72       1794.55                56.08         0.555          pass              0.644             37.4                           0.347               -1.25              0.104                                 ok            True                  False
   HON           88.89               27            0.76              1.30        245.71                40.09         0.532          pass              0.600             65.3                           0.346                7.95              0.900                                 ok            True                  False
  KLAC           85.71               28            1.71              2.61        217.61                98.03         0.706          pass              0.438             31.8                           0.280               -7.14             -0.694 downtrend_blocked_slope_and_streak           False                  False
  AMAT           91.67               24            1.98              7.79        559.46                96.41         0.647          pass              0.588             39.5                           0.331               -8.44             -0.786 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.19               27            1.82              4.07        318.03                88.87         0.639          pass              0.454             46.0                           0.321              -10.38             -0.947 downtrend_blocked_slope_and_streak           False                  False
   KHC           89.47               19            0.24              0.04         25.34                32.50         0.619          pass              0.597             74.0                           0.391                1.80              0.205                                 ok           False                  False
  MDLZ           95.83               24            0.22              0.09         60.01                31.80         0.607          pass              0.664             36.6                           0.207                1.85              0.207                                 ok           False                  False
   KDP           92.59               27            0.39              0.08         29.64                36.62         0.592          pass              0.543             11.5                           0.143               -6.68             -0.540 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-24T10:10:05.990333-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:05:02.385595-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:00:02.441453-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T09:50:06.179967-04:00      manage_1000               exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "AAPL260821C00320000", "fill_price": 13.675, "pnl": 3185.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 21.83, "ticker": "AAPL"}
2026-07-24T00:00:02.342132-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 93}
2026-07-23T15:10:05.971667-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:05:04.134167-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:00:04.002554-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:55:02.141413-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:50:05.030619-04:00       entry_1500              entry {"allocated_cash": 14592.5, "asset_type": "option", "contract_symbol": "AAPL260821C00320000", "contracts": 13, "early_entry_score": 0.378, "entry_mode": "regular", "entry_option_price": 11.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 25201.0, "option_spread_pct": 2.23, "option_volume": 5101.0, "success_rate": 90.0, "ticker": "AAPL", "timing_score": 0.624}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724101005)

</details>
