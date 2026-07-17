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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=346ms, nekobox=346ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-79MS` (url=290ms, nekobox=309ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-91MS` (url=334ms, nekobox=410ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-102MS` (url=335ms, nekobox=353ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-108MS` (url=487ms, nekobox=500ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS` (url=316ms, nekobox=404ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-111MS` (url=419ms, nekobox=394ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=294ms, nekobox=358ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-111MS` (url=355ms, nekobox=393ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS` (url=344ms, nekobox=217ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-131MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-135MS` (url=283ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-112MS` (url=309ms, status=HTTP 204)
14. `AKUN-014-UK-GB-DCL-01-20191003-VLESS-WS-122MS` (url=326ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=365ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-145MS` (url=374ms, status=HTTP 204)
17. `AKUN-017-CCWU-VLESS-WS-153MS` (url=376ms, status=HTTP 204)
18. `AKUN-018-NEXUSMODS-VLESS-WS-156MS` (url=329ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-200MS` (url=329ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-104MS` (url=343ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-181MS` (url=463ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-176MS` (url=337ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-317MS` (url=646ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-315MS` (url=686ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-347MS` (url=693ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
