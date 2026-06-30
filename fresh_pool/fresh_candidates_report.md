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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=262ms, nekobox=281ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-78MS` (url=253ms, nekobox=288ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=235ms, nekobox=300ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=256ms, nekobox=295ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=264ms, nekobox=306ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=267ms, nekobox=291ms, status=yes)
7. `AKUN-007-UK-GB-DCL-01-20191003-VLESS-WS-92MS` (url=290ms, nekobox=280ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=285ms, nekobox=304ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=286ms, nekobox=281ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=242ms, nekobox=286ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS` (url=240ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-94MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-93MS` (url=270ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=286ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=262ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-79MS` (url=298ms, status=HTTP 204)
17. `AKUN-017-DIGITALOCEAN-VLESS-WS-159MS` (url=264ms, status=HTTP 204)
18. `AKUN-018-ZOOM-VLESS-WS-99MS` (url=343ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-222MS` (url=301ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-290MS` (url=613ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-288MS` (url=632ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-275MS` (url=1108ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-294MS` (url=1091ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-317MS` (url=654ms, status=HTTP 204)
25. `AKUN-025-MICROSOFT-VLESS-WS-292MS` (url=683ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
