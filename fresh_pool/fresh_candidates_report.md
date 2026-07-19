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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-82MS` (url=327ms, nekobox=322ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=297ms, nekobox=216ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-85MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-106MS`
5. `AKUN-004-GO-DADDY-COM-LLC-VLESS-WS-102MS`
6. `AKUN-005-ZOOM-VLESS-WS-111MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-93MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-119MS`
9. `AKUN-008-DIXONS-VLESS-WS-118MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-120MS` (url=379ms, nekobox=211ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-80MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-112MS` (url=290ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-110MS` (url=301ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-152MS` (url=378ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=366ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-120MS` (url=296ms, status=HTTP 204)
19. `AKUN-019-UK-GB-DCL-01-20191003-VLESS-WS-121MS` (url=308ms, status=HTTP 204)
20. `AKUN-020-NEXUSMODS-VLESS-WS-146MS` (url=304ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-110MS` (url=306ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-115MS` (url=364ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-157MS` (url=311ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-150MS` (url=320ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-121MS` (url=339ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
