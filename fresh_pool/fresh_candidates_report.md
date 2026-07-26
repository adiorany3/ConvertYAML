# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-UNKNOWN-VLESS-WS-84MS` (url=236ms, nekobox=240ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-89MS` (url=200ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=200ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=201ms, nekobox=234ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-101MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS`
7. `AKUN-007-UNKNOWN-VLESS-WS-105MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-116MS`
10. `AKUN-010-UNKNOWN-VLESS-WS-92MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-119MS` (url=203ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=230ms, status=HTTP 204)
13. `AKUN-015-SKK-VLESS-WS-156MS` (url=261ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-164MS` (url=260ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, status=HTTP 204)
16. `AKUN-018-ZVC-VLESS-WS-89MS` (url=211ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-361MS` (url=5035ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-383MS` (url=4032ms, status=HTTP 204)
19. `AKUN-022-CONFLU-VLESS-WS-419MS` (url=759ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-673MS` (url=2030ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-718MS` (url=1264ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-808MS` (url=1698ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
