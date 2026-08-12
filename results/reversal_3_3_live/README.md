# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 09:40:02 EDT`
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

- Cash: `$17,648.00`
- Equity: `$31,448.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   2      5     13425.0                 13800.0        26.85           27.6      307.66        325.14     last_price_stale                        NaN                unavailable                   False           375.0                   2.79          87.1               31              1.19         68.92             0.0                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
 CMCSA           90.48               21            0.62              0.11         25.60                42.38         0.638          pass              0.575             52.9                           0.400                7.69              0.712                      ok            True                  False
  GEHC           93.33               30            0.93              0.48         72.55                54.33         0.601          pass              0.732             60.9                           0.494                0.24              0.341                      ok            True                  False
  ABNB           96.77               31            1.04              1.35        184.40                64.05         0.592          pass              0.794             64.8                           0.570               19.63              2.325                      ok            True                   True
   ROP           96.88               32            0.58              1.63        398.80                44.32         0.579          pass              0.833             76.2                           0.602                2.03              0.228                      ok            True                   True
  WDAY           82.14               28            2.00              2.54        180.18                68.78         0.546          pass              0.351             39.6                           0.569                5.73              1.209                      ok            True                  False
  ADSK           83.33               36            0.58              1.02        251.15                45.76         0.528          pass              0.544             76.3                           0.609                6.46              0.887                      ok            True                  False
   PEP           83.33               24            0.84              0.82        138.06                20.92         0.517          pass              0.315             27.0                           0.276               -2.11             -0.199                      ok            True                  False
   BKR           83.87               31            0.76              0.34         64.66                33.24         0.514          pass              0.413             39.5                           0.291                7.77              0.841                      ok            True                  False
  REGN           93.55               31            0.84              4.71        794.98                33.78         0.510          pass              0.689             45.7                           0.438                7.03              0.693                      ok            True                  False
  CTSH           84.38               32            1.36              0.56         58.36                52.45         0.501          pass              0.472             53.0                           0.474                7.24              0.750                      ok            True                  False
  MELI           92.86               14            2.26             30.71       1926.84                34.10         0.501          pass              0.436              5.3                           0.108                0.55              0.019                      ok            True                  False
  MNST           92.31               39            0.20              0.06         45.50               245.19         0.978          pass              0.863             81.2                           0.551              -53.51             -6.502 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-12T09:35:01.769154-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:30:01.771593-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:25:01.593760-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:20:03.729351-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:15:01.696450-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:10:04.748220-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:05:02.776077-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T09:00:03.695691-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:55:02.907270-04:00 data_refresh data_refresh {'saved': 93}
2026-08-12T08:50:06.776266-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812094002)

</details>
