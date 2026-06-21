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
1. `AKUN-001-UNKNOWN-VLESS-WS-135MS` (url=303ms, nekobox=311ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-159MS` (url=279ms, nekobox=300ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-167MS` (url=260ms, nekobox=297ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-164MS` (url=251ms, nekobox=305ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-150MS` (url=288ms, nekobox=312ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-176MS` (url=285ms, nekobox=302ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-178MS` (url=290ms, nekobox=296ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS` (url=268ms, nekobox=305ms, status=yes)
9. `AKUN-009-VULTR-VLESS-WS-177MS` (url=263ms, nekobox=313ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-166MS` (url=267ms, nekobox=306ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=266ms, status=HTTP 204)
12. `AKUN-012-VULTR-VLESS-WS-133MS` (url=264ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-170MS` (url=272ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-168MS` (url=277ms, status=HTTP 204)
15. `AKUN-015-CONFLU-VLESS-WS-360MS` (url=689ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-379MS` (url=838ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-386MS` (url=819ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-154MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-387MS` (url=746ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-400MS` (url=809ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-151MS` (url=301ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-353MS` (url=693ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-380MS` (url=766ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-663MS` (url=1145ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-746MS` (url=2345ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
