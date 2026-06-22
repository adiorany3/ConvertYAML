# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=279ms, nekobox=315ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-147MS` (url=300ms, nekobox=302ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-143MS` (url=320ms, nekobox=314ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-150MS` (url=260ms, nekobox=309ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-146MS` (url=325ms, nekobox=309ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-141MS` (url=281ms, nekobox=296ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-148MS` (url=310ms, nekobox=302ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS` (url=284ms, nekobox=319ms, status=yes)
9. `AKUN-009-UK-GB-DCL-01-20191003-VLESS-WS-170MS` (url=368ms, nekobox=339ms, status=yes)
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-150MS` (url=292ms, nekobox=307ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-172MS` (url=313ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-165MS` (url=290ms, status=HTTP 204)
13. `AKUN-013-OPENAI-VLESS-WS-153MS` (url=300ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-183MS` (url=300ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-285MS` (url=364ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-396MS` (url=774ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-385MS` (url=724ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-402MS` (url=788ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-415MS` (url=767ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-406MS` (url=818ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-157MS` (url=282ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-664MS` (url=2350ms, status=HTTP 204)
23. `AKUN-030-RS-RAPIDSEEDBOX-20190717-VLESS-WS-716MS` (url=1089ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-825MS` (url=5227ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
