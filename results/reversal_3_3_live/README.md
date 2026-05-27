# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 11:20:01 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$19,575.25`
- Equity: `$31,765.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12190.0        60.05          60.95       531.8        524.09          bid_ask_mid                      60.95                bid_ask_mid                    True           180.0                    1.5         97.22               36              0.52         54.56           62.27                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            1.03              2.40        331.64                92.16         0.634          pass              0.537             42.3                           0.403               11.90              1.210                                 ok            True                  False
  ISRG           85.71               14            2.16              6.60        433.81                35.34         0.522          pass              0.287             18.6                           0.364               -1.08              0.148                                 ok            True                  False
  ASML           88.89               27            1.89             21.54       1622.80                54.27         0.511          pass              0.513             37.2                           0.404                5.28              0.583                                 ok            True                  False
  UPRO           94.29               35            0.51              0.52        145.64                30.88         0.501          pass              0.617              6.3                           0.190                4.01              0.276                                 ok            True                  False
  INSM           67.86               28            1.76              1.34        108.30               110.60         0.737          pass              0.206              4.2                           0.280               -7.80             -0.879            downtrend_blocked_slope           False                  False
    MU           83.78               37            0.14              0.90        895.49               103.81         0.645          pass              0.595             83.3                           0.406               16.70              1.164                                 ok           False                  False
   AEP           80.00               20            0.32              0.29        130.77                25.21         0.595          pass              0.342             72.0                           0.677               -1.11              0.167                                 ok           False                  False
  REGN           86.21               29            0.97              4.32        632.77                48.91         0.582          pass              0.458             35.8                           0.281              -13.00             -1.499 downtrend_blocked_slope_and_streak           False                  False
  INTC           92.31               13            4.22              3.65        121.96                91.80         0.569          pass              0.463             19.2                           0.229               -1.91              0.341           downtrend_blocked_streak           False                  False
  ORLY           68.75               16            1.51              0.95         89.46                38.82         0.546          pass              0.138             14.5                           0.188               -3.63             -0.017                                 ok           False                  False
  FTNT          100.00                3            5.14              4.82        131.90                66.88         0.539          pass              0.495             13.6                           0.142               11.60              1.348                                 ok           False                  False
  NVDA           70.00               10            2.62              3.94        213.17                40.94         0.503          pass              0.072              7.4                           0.218               -5.23             -0.715 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:10:01.701881-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:05:03.689642-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T11:00:02.698480-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:55:01.700501-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:50:01.641792-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:35:01.630649-04:00 early_entry_1035         entry {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SNPS260717C00500000", "contracts": 2, "early_entry_score": 0.805, "entry_mode": "early", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 9.83, "option_volume": 157.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.413}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527112001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527112001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527112001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527112001)

</details>
