# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 10:50:06 EDT`
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

- Cash: `$17,469.25`
- Equity: `$34,194.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$525.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AMZN     option         option AMZN260717C00260000       2026-06-02                   0     15     16200.0                 16725.0         10.8          11.15      259.57        259.42          bid_ask_mid                      11.15                bid_ask_mid                    True           525.0                   3.24         90.62               32              0.65         30.52           31.23                  24.44                8913.0          913.0               0.02                      ok
```

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           84.85               33            1.01              7.32       1031.60               101.73         0.716          pass              0.493             46.3                           0.214               50.29              4.595                                 ok            True                  False
  FTNT          100.00               15            1.92              1.97        146.29                71.69         0.676          pass              0.667             55.4                           0.610               14.09              1.240                                 ok            True                  False
  MELI           92.00               25            1.76             21.29       1721.86                60.28         0.597          pass              0.601             40.3                           0.561                7.23              0.724                                 ok            True                  False
  INTC           96.55               29            1.27              0.97        108.91                88.85         0.571          pass              0.803             73.1                           0.855               -0.21             -0.107                                 ok            True                  False
  AMGN           90.00               20            0.82              1.89        328.32                20.27         0.518          pass              0.567             60.5                           0.749                0.63              0.039                                 ok            True                  False
  INSM           62.50               16            3.16              2.35        105.02               110.78         0.710          pass              0.227             38.7                           0.647               -4.18             -0.284            downtrend_blocked_slope           False                  False
  MNST           87.50                8            2.10              1.31         88.54                49.60         0.646          pass              0.265              0.0                           0.157               -1.48              0.144                                 ok           False                  False
   WMT           76.92               13            1.35              1.08        114.14                32.65         0.575          pass              0.109             10.4                           0.185              -15.22             -1.709 downtrend_blocked_slope_and_streak           False                  False
    ZS          100.00                2            8.94              9.74        151.53               157.27         0.570          pass              0.475              6.1                           0.109              -18.83             -2.815            downtrend_blocked_slope           False                  False
  REGN           88.89               36            0.45              1.90        599.85                42.53         0.536          pass              0.675             70.4                           0.735               -4.90             -0.625 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.78              2.95        235.27                24.20         0.528          pass              0.065              4.2                           0.100                6.95              0.949                                 ok           False                  False
   ADP          100.00                7            2.87              4.69        231.73                34.26         0.503          pass              0.515             21.5                           0.324                1.84              0.277                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T10:50:06.041869-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:45:01.434257-04:00 early_entry_1045                   entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
2026-06-02T10:40:04.457109-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:30:04.405006-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:25:01.235572-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:20:01.327977-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-06-02T10:15:02.269482-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                                               {"early_entry_score": 0.679, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 117.0, "option_spread_pct": 24.24, "option_volume": 5.0, "reason": "no_trade_low_option_liquidity", "ticker": "CHTR", "timing_score": 0.442}
2026-06-02T10:10:06.260122-04:00 early_entry_1010           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602105006)

</details>
