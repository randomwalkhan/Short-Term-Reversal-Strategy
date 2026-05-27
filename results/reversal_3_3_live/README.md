# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 12:50:02 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$31,105.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 11530.0        60.05          57.65       531.8        527.73          bid_ask_mid                      57.65                bid_ask_mid                    True          -480.0                   -4.0         97.22               36              0.52         54.56           55.02                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           95.45               22            3.01              2.60        122.40                91.80         0.591          pass              0.666             42.4                           0.640               -0.67              0.398                                 ok            True                  False
  SOXL           85.71               21            4.23              6.68        222.93               148.29         0.511          pass              0.445             56.2                           0.601               25.35              2.101                                 ok            True                  False
  ASML           89.29               28            1.82             20.80       1623.11                54.27         0.509          pass              0.537             39.4                           0.422                5.35              0.586                                 ok            True                  False
  LRCX           83.33               30            1.04              2.35        321.67                57.65         0.501          pass              0.452             60.0                           0.600               10.40              0.980                                 ok            True                  False
  INSM           67.86               28            1.86              1.42        108.26               110.60         0.724          pass              0.276             28.0                           0.425               -7.90             -0.884            downtrend_blocked_slope           False                  False
  NXPI           89.74               39            0.21              0.49        332.46                92.16         0.643          pass              0.782             88.2                           0.801               12.83              1.247                                 ok           False                  False
   AEP           66.67               12            0.73              0.67        130.61                25.21         0.605          pass              0.183             36.3                           0.262               -1.51              0.148                                 ok           False                  False
  REGN           86.67               30            0.89              3.96        632.92                48.91         0.581          pass              0.493             41.2                           0.386              -12.93             -1.495 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00                6            4.24              3.98        132.25                66.88         0.575          pass              0.543             28.6                           0.310               12.65              1.391                                 ok           False                  False
  PAYX           95.83               24            0.29              0.19         94.72                30.13         0.571          pass              0.703             50.9                           0.301                2.17              0.587                                 ok           False                  False
  GEHC           73.53               34            0.86              0.38         64.02                58.90         0.565          pass              0.322             35.3                           0.440                2.15              0.439                                 ok           False                  False
  ORLY           73.33               15            1.61              1.01         89.44                38.82         0.552          pass              0.121             10.8                           0.247               -3.72             -0.021                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-27T12:00:02.710964-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:50:03.680135-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:45:03.631384-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:40:05.644907-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:35:01.763028-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:30:03.642153-04:00 early_entry_1130 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:25:02.657208-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:20:01.673157-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-27T11:15:01.657140-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527125002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527125002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527125002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527125002)

</details>
