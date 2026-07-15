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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=283ms, nekobox=324ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=284ms, nekobox=331ms, status=yes)
3. `AKUN-003-ORACLE-VLESS-WS-93MS` (url=288ms, nekobox=307ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-107MS` (url=283ms, nekobox=318ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-114MS` (url=277ms, nekobox=366ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-115MS` (url=300ms, nekobox=363ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS` (url=336ms, nekobox=315ms, status=yes)
8. `AKUN-008-GO-DADDY-COM-LLC-VLESS-WS-115MS` (url=300ms, nekobox=327ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-119MS` (url=384ms, nekobox=387ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-123MS` (url=283ms, nekobox=345ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-108MS` (url=281ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-124MS` (url=338ms, status=HTTP 204)
13. `AKUN-013-ORG-VLESS-WS-103MS` (url=285ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-138MS` (url=313ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-115MS` (url=311ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-147MS` (url=320ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-147MS` (url=339ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-122MS` (url=318ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-135MS` (url=357ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-158MS` (url=303ms, status=HTTP 204)
21. `AKUN-021-POLICE-VLESS-WS-146MS` (url=361ms, status=HTTP 204)
22. `AKUN-022-NEXUSMODS-VLESS-WS-136MS` (url=467ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-311MS` (url=677ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-327MS` (url=650ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-337MS` (url=697ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
