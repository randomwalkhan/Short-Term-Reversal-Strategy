# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:05:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$14,107.75`
- Equity: `$27,792.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,330.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13685.0         8.82           9.78      126.75         128.1          bid_ask_mid                       9.78                bid_ask_mid                    True          1330.0                  10.76         100.0               38              0.69         41.39            41.4                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.55               31            0.57              1.20        301.80                69.06         0.626            pass              0.821             85.6                           0.424                3.85              0.571                                 ok            True                  False
   WMT           90.91               11            1.38              1.29        133.65                20.68         0.533            pass              0.528             59.2                           0.610                1.94              0.333                                 ok            True                  False
  ADSK           90.91               22            1.34              2.29        243.18                38.52         0.512            pass              0.633             70.2                           0.723               -0.90             -0.153                                 ok            True                  False
  CTSH           88.00               25            1.21              0.43         50.70                50.98         0.512            pass              0.570             68.5                           0.717               -1.38             -0.221                                 ok            True                  False
 GOOGL           88.24               34            0.65              1.77        386.90                41.27         0.503            pass              0.570             46.8                           0.419               -3.24             -0.203                                 ok            True                  False
  TEAM           88.57               35            1.62              0.98         86.20               114.61         0.624            pass              0.663             68.3                           0.720               -4.03             -0.528 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.45               22            0.23              0.15         94.41                29.36         0.559            pass              0.814             92.7                           0.773                4.48              0.245                                 ok           False                  False
  TMUS           78.57               14            2.16              2.93        192.16                36.70         0.505            pass              0.084              2.3                           0.140               -2.03             -0.229                                 ok           False                  False
  AMGN           84.00               25            0.55              1.28        330.20                26.77         0.499 below_threshold              0.500             81.0                           0.496                0.09              0.005                                 ok           False                  False
   KDP           89.47               38            0.19              0.04         28.83                34.80         0.497 below_threshold              0.758             89.5                           0.754                0.82              0.147                                 ok           False                  False
  SNPS           97.37               38            0.28              0.98        493.45                41.71         0.496 below_threshold              0.915             93.0                           0.853               -2.37             -0.343 downtrend_blocked_slope_and_streak           False                  False
  GOOG           87.88               33            0.68              1.84        384.11                41.08         0.496 below_threshold              0.552             46.3                           0.406               -3.26             -0.213           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-20T11:05:01.079772-04:00 early_entry_1105           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:30:01.058983-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:25:06.944713-04:00 early_entry_1025                   entry {"allocated_cash": 12355.0, "asset_type": "option", "contract_symbol": "FTNT260717C00125000", "contracts": 14, "early_entry_score": 0.837, "entry_mode": "early", "entry_option_price": 8.825, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 1300.0, "option_spread_pct": 11.9, "option_volume": 40.0, "success_rate": 100.0, "ticker": "FTNT", "timing_score": 0.622}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.683, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 46.51, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTAS", "timing_score": 0.458}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520110501)

</details>
