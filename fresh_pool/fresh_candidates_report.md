# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=215ms, nekobox=238ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-60MS` (url=211ms, nekobox=223ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-56MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-84MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-67MS`
8. `AKUN-008-FASTVPSUS-IPV4-VLESS-WS-111MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-64MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-78MS` (url=201ms, status=HTTP 204)
12. `AKUN-013-EE-WELCOMEHOST-20190515-VLESS-WS-126MS` (url=219ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-86MS` (url=197ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-76MS` (url=226ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-145MS` (url=217ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-127MS` (url=216ms, status=HTTP 204)
17. `AKUN-018-090227-VLESS-WS-135MS` (url=343ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-166MS` (url=704ms, status=HTTP 204)
19. `AKUN-022-UNKNOWN-VLESS-WS-394MS` (url=646ms, status=HTTP 204)
20. `AKUN-023-SUKARIO-VLESS-WS-400MS` (url=654ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-410MS` (url=693ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-504MS` (url=1720ms, status=HTTP 204)
23. `AKUN-028-UNKNOWN-VLESS-WS-506MS` (url=901ms, status=HTTP 204)
24. `AKUN-029-SPEEDTEST-VLESS-WS-501MS` (url=744ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-510MS` (url=837ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
