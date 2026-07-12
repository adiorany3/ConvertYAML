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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-129MS` (url=270ms, nekobox=291ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-135MS` (url=273ms, nekobox=301ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-130MS` (url=298ms, nekobox=301ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-140MS` (url=269ms, nekobox=301ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-132MS` (url=272ms, nekobox=292ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=257ms, nekobox=228ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-136MS`
8. `AKUN-007-ORACLE-VLESS-WS-143MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-134MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-146MS`
11. `AKUN-010-ZVC-VLESS-WS-147MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-137MS` (url=272ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-151MS` (url=307ms, status=HTTP 204)
14. `AKUN-014-TENCENT-VLESS-WS-158MS` (url=283ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-150MS` (url=353ms, status=HTTP 204)
16. `AKUN-016-NET-82-21-84-0-24-VLESS-WS-160MS` (url=303ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-149MS` (url=333ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=277ms, status=HTTP 204)
19. `AKUN-019-PUBLICDOMAINREGISTRY-NET-VLESS-WS-179MS` (url=308ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-151MS` (url=296ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-249MS` (url=435ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-350MS` (url=752ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-361MS` (url=800ms, status=HTTP 204)
24. `AKUN-026-UK-GB-DCL-01-20191003-VLESS-WS-370MS` (url=789ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-385MS` (url=814ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
