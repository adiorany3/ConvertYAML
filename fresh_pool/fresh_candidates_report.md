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
1. `AKUN-001-UNKNOWN-VLESS-WS-89MS` (url=213ms, nekobox=237ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=210ms, nekobox=266ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-95MS` (url=215ms, nekobox=244ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-95MS` (url=207ms, nekobox=232ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-98MS` (url=210ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=224ms, nekobox=242ms, status=yes)
7. `AKUN-007-466688-VLESS-WS-90MS` (url=225ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-110MS` (url=278ms, nekobox=258ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-102MS` (url=209ms, nekobox=274ms, status=yes)
10. `AKUN-010-IONOS-VLESS-WS-120MS` (url=237ms, nekobox=263ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-106MS` (url=220ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-109MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=212ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-120MS` (url=245ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-134MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-135MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-140MS` (url=259ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-160MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=244ms, status=HTTP 204)
20. `AKUN-020-PUBLICDOMAINREGISTRY-NET-VLESS-WS-159MS` (url=220ms, status=HTTP 204)
21. `AKUN-021-DE-XTOM-20190821-VLESS-WS-117MS` (url=214ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-151MS` (url=248ms, status=HTTP 204)
23. `AKUN-023-SPEEDTEST-VLESS-WS-378MS` (url=880ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-381MS` (url=793ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-400MS` (url=801ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
