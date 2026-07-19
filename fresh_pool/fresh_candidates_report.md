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
1. `AKUN-001-GOV-VLESS-WS-62MS` (url=218ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=206ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-61MS` (url=205ms, nekobox=231ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-65MS` (url=263ms, nekobox=235ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-70MS` (url=930ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=213ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS` (url=216ms, nekobox=233ms, status=yes)
8. `AKUN-008-DIXONS-VLESS-WS-92MS` (url=227ms, nekobox=239ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-76MS` (url=209ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=202ms, nekobox=229ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-80MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-90MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-115MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-112MS` (url=207ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-92MS` (url=203ms, status=HTTP 204)
17. `AKUN-017-NEXUSMODS-VLESS-WS-120MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-126MS` (url=241ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=204ms, status=HTTP 204)
20. `AKUN-020-466688-VLESS-WS-144MS` (url=219ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-149MS` (url=217ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-175MS` (url=216ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-240MS` (url=522ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-235MS` (url=487ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-244MS` (url=4346ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
