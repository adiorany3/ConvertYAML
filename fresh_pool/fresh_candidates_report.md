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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=216ms, nekobox=264ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=235ms, nekobox=271ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-70MS` (url=240ms, nekobox=246ms, status=yes)
4. `AKUN-004-PUBLICDOMAINREGISTRY-NET-VLESS-WS-72MS` (url=252ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=223ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS` (url=225ms, nekobox=266ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-62MS` (url=218ms, nekobox=242ms, status=yes)
8. `AKUN-008-US-VLESS-WS-96MS` (url=241ms, nekobox=276ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-81MS` (url=245ms, nekobox=276ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-71MS` (url=225ms, nekobox=7177ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-106MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-120MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-69MS` (url=216ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-122MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-84MS` (url=236ms, status=HTTP 204)
17. `AKUN-017-ES-FORNEX-20160629-VLESS-WS-101MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=233ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-91MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-72MS` (url=659ms, status=HTTP 204)
21. `AKUN-021-MEDIUM-VLESS-WS-161MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-254MS` (url=556ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-235MS` (url=493ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-367MS` (url=770ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-381MS` (url=798ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
