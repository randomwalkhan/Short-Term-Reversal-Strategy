# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 11:10:02 EDT`
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
- Equity: `$27,512.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$1,050.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 13405.0         8.82           9.57      126.75        128.23          bid_ask_mid                       9.57                bid_ask_mid                    True          1050.0                    8.5         100.0               38              0.69         41.39           40.29                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.55               31            0.57              1.20        301.79                69.06         0.626            pass              0.821             85.5                           0.411                3.85              0.571                                 ok            True                  False
   WMT           91.67               12            1.28              1.20        133.68                20.68         0.534            pass              0.564             62.0                           0.612                2.04              0.338                                 ok            True                  False
 GOOGL           86.21               29            0.88              2.39        386.64                41.27         0.519            pass              0.429             28.4                           0.315               -3.46             -0.213                                 ok            True                  False
  CTSH           88.89               27            1.12              0.40         50.71                50.98         0.505            pass              0.613             70.8                           0.750               -1.30             -0.217                                 ok            True                  False
  AMGN           83.33               24            0.63              1.47        330.12                26.77         0.500 below_threshold              0.467             78.2                           0.470                0.01              0.001                                 ok            True                  False
  TEAM           88.89               36            1.58              0.96         86.21               114.61         0.620            pass              0.679             69.0                           0.721               -4.00             -0.527 downtrend_blocked_slope_and_streak           False                  False
  PAYX           95.45               22            0.24              0.16         94.41                29.36         0.559            pass              0.813             92.5                           0.777                4.47              0.245                                 ok           False                  False
  GOOG           85.71               28            0.90              2.43        383.86                41.08         0.512            pass              0.411             29.1                           0.303               -3.47             -0.223           downtrend_blocked_streak           False                  False
  TMUS           76.92               13            2.18              2.95        192.16                36.70         0.507            pass              0.100              9.7                           0.159               -2.04             -0.230                                 ok           False                  False
   KDP           88.89               36            0.26              0.05         28.83                34.80         0.505            pass              0.718             85.7                           0.705                0.75              0.144                                 ok           False                  False
  ADSK           89.29               28            1.02              1.74        243.42                38.52         0.490 below_threshold              0.649             77.4                           0.755               -0.58             -0.138                                 ok           False                  False
   TRI           75.00               12            2.57              1.57         86.68                57.28         0.488 below_threshold              0.199             45.6                           0.306               -7.24             -0.899 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-20T11:10:02.083171-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T11:05:01.079772-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T11:00:03.973296-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:55:04.047991-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:50:01.057025-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:30:01.058983-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:25:06.944713-04:00 early_entry_1025         entry {"allocated_cash": 12355.0, "asset_type": "option", "contract_symbol": "FTNT260717C00125000", "contracts": 14, "early_entry_score": 0.837, "entry_mode": "early", "entry_option_price": 8.825, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 1300.0, "option_spread_pct": 11.9, "option_volume": 40.0, "success_rate": 100.0, "ticker": "FTNT", "timing_score": 0.622}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520111002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520111002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520111002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520111002)

</details>
