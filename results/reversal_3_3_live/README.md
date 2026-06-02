# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 11:20:04 EDT`
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

- Cash: `$17,469.25`
- Equity: `$35,731.75`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$2,062.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AMZN     option         option AMZN260717C00260000       2026-06-02                   0     15     16200.0                 18262.5         10.8          12.18      259.57        260.79          bid_ask_mid                      12.18                bid_ask_mid                    True          2062.5                  12.73         90.62               32              0.65         30.52           32.14                  24.44                8913.0          913.0               0.02                      ok
```

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           92.86               14            1.60              1.00         88.67                49.60         0.645          pass              0.504             23.5                           0.440               -0.98              0.167                                 ok            True                  False
  MELI           86.67               15            2.34             28.38       1718.82                60.28         0.619          pass              0.334             20.5                           0.235                6.59              0.697                                 ok            True                  False
  INTC           96.97               33            0.91              0.69        109.03                88.85         0.570          pass              0.853             80.8                           0.721                0.16             -0.091                                 ok            True                   True
  CDNS          100.00               11            2.46              7.13        411.10                44.19         0.546          pass              0.528             22.3                           0.248               16.76              1.700                                 ok            True                  False
  AMGN           90.00               20            0.80              1.84        328.34                20.27         0.520          pass              0.570             61.6                           0.654                0.65              0.040                                 ok            True                  False
  FTNT          100.00                9            2.34              2.41        146.11                71.69         0.687          pass              0.605             45.4                           0.339               13.59              1.220                                 ok           False                  False
  INSM           45.45               11            4.11              3.05        104.72               110.78         0.666          pass              0.134             20.3                           0.260               -5.11             -0.329            downtrend_blocked_slope           False                  False
   WMT           76.92               13            1.32              1.06        114.15                32.65         0.577          pass              0.116             12.7                           0.287              -15.19             -1.707 downtrend_blocked_slope_and_streak           False                  False
  REGN           88.24               34            0.52              2.20        599.72                42.53         0.544          pass              0.631             65.5                           0.661               -4.97             -0.629 downtrend_blocked_slope_and_streak           False                  False
   HON           71.43                7            1.72              2.85        235.32                24.20         0.532          pass              0.080              8.8                           0.270                7.02              0.952                                 ok           False                  False
    ZS          100.00                2            9.52             10.38        151.26               157.27         0.522          pass              0.469              5.6                           0.212              -19.35             -2.844            downtrend_blocked_slope           False                  False
 GOOGL           84.62               13            1.69              4.46        374.46                26.14         0.514          pass              0.388             64.4                           0.539               -6.79             -0.462            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-02T11:20:04.407163-04:00 early_entry_1120 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:15:04.236525-04:00 early_entry_1115 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:10:04.323542-04:00 early_entry_1110 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:05:01.381854-04:00 early_entry_1105 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T11:00:04.363054-04:00 early_entry_1100 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:55:06.617729-04:00 early_entry_1055 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:50:06.041869-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-06-02T10:45:01.434257-04:00 early_entry_1045         entry {"allocated_cash": 16200.0, "asset_type": "option", "contract_symbol": "AMZN260717C00260000", "contracts": 15, "early_entry_score": 0.702, "entry_mode": "early", "entry_option_price": 10.8, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 8913.0, "option_spread_pct": 1.85, "option_volume": 913.0, "success_rate": 90.62, "ticker": "AMZN", "timing_score": 0.457}
2026-06-02T10:40:04.457109-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
2026-06-02T10:35:04.553797-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602112004)

</details>
